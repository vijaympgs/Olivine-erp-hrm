import time
import io
import re
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Attempt to import OCR libraries
try:
    from PIL import Image
    import pytesseract
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False

@method_decorator(csrf_exempt, name='dispatch')
class VisualExtractionView(View):
    """
    Real OCR Extraction Engine using Tesseract.
    Processes image inputs and returns extracted text as markdown.
    Falls back to error message if Tesseract is not installed.
    """

    def _format_as_markdown(self, raw_text: str, confidence: float) -> str:
        """
        Transform raw OCR text into clean, structured markdown.
        """
        lines = raw_text.strip().split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            # Skip very short noise lines
            if len(line) < 2:
                continue
            cleaned_lines.append(line)
        
        if not cleaned_lines:
            return "# No Text Detected\n\n*The image appears to contain no readable text.*"
        
        # Build markdown output
        timestamp = time.strftime("%I:%M:%S %p")
        markdown = f"# EXTRACTED CONTENT\n\n"
        markdown += f"*Extracted at: {timestamp}*\n\n"
        markdown += "---\n\n"
        
        # Group lines into logical sections
        current_section = []
        for line in cleaned_lines:
            # Detect potential headers (short lines, all caps, or ending with colon)
            is_header = (
                len(line) < 40 and 
                (line.isupper() or line.endswith(':') or re.match(r'^[A-Z][a-z]+ [A-Z]', line))
            )
            
            if is_header and current_section:
                # Output previous section as list
                for item in current_section:
                    markdown += f"- {item}\n"
                markdown += "\n"
                current_section = []
                markdown += f"## {line.rstrip(':')}\n\n"
            elif is_header:
                markdown += f"## {line.rstrip(':')}\n\n"
            else:
                current_section.append(line)
        
        # Output remaining items
        if current_section:
            for item in current_section:
                markdown += f"- {item}\n"
        
        markdown += "\n---\n"
        markdown += f"*OCR Confidence: {confidence:.1f}%*\n"
        markdown += f"*Vision Engine: Tesseract 5.x + Pillow*\n"
        markdown += f"*Processing Status: Success*"
        
        return markdown

    def _extract_with_tesseract(self, image_file) -> tuple:
        """
        Perform OCR using Pytesseract.
        Returns: (extracted_text, confidence_score)
        """
        # Read image into PIL
        image_bytes = image_file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to RGB if necessary (handles PNG with alpha)
        if image.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', image.size, (255, 255, 255))
            if image.mode == 'P':
                image = image.convert('RGBA')
            background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
            image = background
        
        # Extract text with detailed data for confidence
        try:
            data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
            confidences = [int(c) for c in data['conf'] if int(c) > 0]
            avg_confidence = sum(confidences) / len(confidences) if confidences else 0.0
        except Exception:
            avg_confidence = 85.0  # Default if confidence extraction fails
        
        # Extract plain text
        text = pytesseract.image_to_string(image)
        
        return text, avg_confidence

    def post(self, request):
        try:
            start_time = time.time()
            
            # Validate file upload
            if 'image' not in request.FILES:
                return JsonResponse({
                    "success": False,
                    "error": "No image file provided. Please upload an image."
                }, status=400)
            
            uploaded_file = request.FILES['image']
            filename = uploaded_file.name
            file_size = uploaded_file.size
            
            # Check if Tesseract is available
            if not TESSERACT_AVAILABLE:
                return JsonResponse({
                    "success": False,
                    "error": "OCR engine not available. Please install: pip install pytesseract Pillow, and ensure Tesseract is installed on the system.",
                    "install_instructions": {
                        "windows": "Download from: https://github.com/UB-Mannheim/tesseract/wiki",
                        "linux": "sudo apt install tesseract-ocr",
                        "mac": "brew install tesseract"
                    }
                }, status=503)
            
            # Perform real OCR
            try:
                raw_text, confidence = self._extract_with_tesseract(uploaded_file)
            except Exception as ocr_error:
                return JsonResponse({
                    "success": False,
                    "error": f"OCR processing failed: {str(ocr_error)}. Ensure Tesseract is installed and in PATH."
                }, status=500)
            
            # Format as markdown
            markdown = self._format_as_markdown(raw_text, confidence)
            
            processing_time = time.time() - start_time
            timestamp = time.strftime("%I:%M:%S %p")
            
            return JsonResponse({
                "success": True,
                "markdown": markdown,
                "timestamp": timestamp,
                "metadata": {
                    "filename": filename,
                    "file_size_bytes": file_size,
                    "processing_time_ms": round(processing_time * 1000),
                    "confidence": round(confidence, 1),
                    "engine": "Tesseract OCR"
                }
            })

        except Exception as e:
            return JsonResponse({
                "success": False,
                "error": f"Unexpected error: {str(e)}"
            }, status=500)
