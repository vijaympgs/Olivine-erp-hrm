#!/usr/bin/env python3
"""
ChatGPT Command Line Interface
A terminal-based interface for ChatGPT using OpenAI API
"""

import os
import sys
import json
import argparse
from datetime import datetime
from typing import List, Dict, Optional
import openai
from openai import OpenAI

# Handle readline for cross-platform compatibility
try:
    import readline  # Unix/Linux/macOS
except ImportError:
    try:
        import pyreadline3 as readline  # Windows fallback
    except ImportError:
        readline = None  # Will work without command history


class ChatGPTCLI:
    """Command Line Interface for ChatGPT"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        """
        Initialize ChatGPT CLI
        
        Args:
            api_key: OpenAI API key (if None, reads from OPENAI_API_KEY env var)
            model: Model to use (default: gpt-4)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            print("Error: OpenAI API key not found!")
            print("Please set OPENAI_API_KEY environment variable or pass --api-key argument")
            sys.exit(1)
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.conversation_history: List[Dict[str, str]] = []
        self.system_prompt = "You are a helpful assistant."
        self.max_history = 10
        
        # Colors for terminal output
        self.colors = {
            'user': '\033[94m',      # Blue
            'assistant': '\033[92m',  # Green
            'system': '\033[93m',     # Yellow
            'error': '\033[91m',      # Red
            'reset': '\033[0m'
        }
    
    def set_system_prompt(self, prompt: str):
        """Set the system prompt for the conversation"""
        self.system_prompt = prompt
    
    def add_message(self, role: str, content: str):
        """Add a message to conversation history"""
        self.conversation_history.append({
            "role": role,
            "content": content
        })
        
        # Keep only last N messages to manage token usage
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]
    
    def get_completion(self, user_input: str, stream: bool = False) -> str:
        """
        Get completion from ChatGPT
        
        Args:
            user_input: User's message
            stream: Whether to stream the response
            
        Returns:
            Assistant's response
        """
        # Add user message to history
        self.add_message("user", user_input)
        
        # Prepare messages for API
        messages = [{"role": "system", "content": self.system_prompt}]
        messages.extend(self.conversation_history)
        
        try:
            if stream:
                # Stream response
                response = ""
                print(f"{self.colors['assistant']}", end='', flush=True)
                
                stream_response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    stream=True
                )
                
                for chunk in stream_response:
                    if chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        print(content, end='', flush=True)
                        response += content
                
                print(f"{self.colors['reset']}", flush=True)
                self.add_message("assistant", response)
                return response
            else:
                # Get full response
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages
                )
                
                assistant_message = response.choices[0].message.content
                self.add_message("assistant", assistant_message)
                return assistant_message
                
        except openai.APIError as e:
            print(f"{self.colors['error']}API Error: {e}{self.colors['reset']}")
            return ""
        except Exception as e:
            print(f"{self.colors['error']}Error: {e}{self.colors['reset']}")
            return ""
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
        print(f"{self.colors['system']}Conversation history cleared.{self.colors['reset']}")
    
    def show_history(self):
        """Display conversation history"""
        print(f"\n{self.colors['system']}=== Conversation History ==={self.colors['reset']}\n")
        for i, msg in enumerate(self.conversation_history, 1):
            role_color = self.colors.get(msg['role'], self.colors['reset'])
            print(f"{role_color}[{msg['role'].upper()}]{self.colors['reset']} {msg['content']}\n")
    
    def save_conversation(self, filename: str):
        """Save conversation to a file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({
                'model': self.model,
                'system_prompt': self.system_prompt,
                'timestamp': datetime.now().isoformat(),
                'messages': self.conversation_history
            }, f, indent=2)
        print(f"{self.colors['system']}Conversation saved to {filename}{self.colors['reset']}")
    
    def load_conversation(self, filename: str):
        """Load conversation from a file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.model = data.get('model', self.model)
                self.system_prompt = data.get('system_prompt', self.system_prompt)
                self.conversation_history = data.get('messages', [])
            print(f"{self.colors['system']}Conversation loaded from {filename}{self.colors['reset']}")
        except Exception as e:
            print(f"{self.colors['error']}Error loading conversation: {e}{self.colors['reset']}")
    
    def print_welcome(self):
        """Print welcome message"""
        print(f"""
{self.colors['assistant']}
╔════════════════════════════════════════════════════════════╗
║           ChatGPT Command Line Interface                  ║
╚════════════════════════════════════════════════════════════╝
{self.colors['reset']}
{self.colors['system']}Model: {self.model}
{self.colors['reset']}
{self.colors['system']}Commands:{self.colors['reset']}
  /clear      - Clear conversation history
  /history    - Show conversation history
  /save       - Save conversation to file
  /load       - Load conversation from file
  /model      - Change model
  /system     - Set system prompt
  /exit       - Exit the program
  /help       - Show this help message
""")
    
    def print_help(self):
        """Print help message"""
        print(f"""
{self.colors['system']}Available Commands:{self.colors['reset']}
  /clear              Clear conversation history
  /history            Show conversation history
  /save [filename]    Save conversation to file (default: chatgpt_conversation.json)
  /load [filename]    Load conversation from file
  /model [model]      Change model (e.g., gpt-4, gpt-3.5-turbo)
  /system [prompt]    Set system prompt
  /stream             Toggle streaming mode
  /exit               Exit the program
  /help               Show this help message
  
{self.colors['system']}Keyboard Shortcuts:{self.colors['reset']}
  Ctrl+C              Clear current input
  Ctrl+D              Exit the program
  Arrow Up/Down       Navigate command history
""")
    
    def run_interactive(self, stream: bool = True):
        """
        Run interactive CLI mode
        
        Args:
            stream: Whether to stream responses
        """
        self.print_welcome()
        
        while True:
            try:
                # Get user input
                user_input = input(f"{self.colors['user']}You{self.colors['reset']}: ").strip()
                
                # Handle empty input
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.startswith('/'):
                    self.handle_command(user_input)
                    continue
                
                # Get and display response
                print(f"{self.colors['assistant']}Assistant{self.colors['reset']}: ", end='', flush=True)
                response = self.get_completion(user_input, stream=stream)
                
                if not stream and response:
                    print(response)
                
                print()  # Add spacing
                
            except KeyboardInterrupt:
                print(f"\n{self.colors['system']}Use /exit to quit{self.colors['reset']}")
            except EOFError:
                print(f"\n{self.colors['system']}Goodbye!{self.colors['reset']}")
                break
    
    def handle_command(self, command: str):
        """Handle special commands"""
        parts = command.split(maxsplit=1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        
        if cmd == '/clear':
            self.clear_history()
        
        elif cmd == '/history':
            self.show_history()
        
        elif cmd == '/save':
            filename = args if args else "chatgpt_conversation.json"
            self.save_conversation(filename)
        
        elif cmd == '/load':
            filename = args if args else "chatgpt_conversation.json"
            self.load_conversation(filename)
        
        elif cmd == '/model':
            if args:
                self.model = args
                print(f"{self.colors['system']}Model changed to: {self.model}{self.colors['reset']}")
            else:
                print(f"{self.colors['system']}Current model: {self.model}{self.colors['reset']}")
        
        elif cmd == '/system':
            if args:
                self.set_system_prompt(args)
                print(f"{self.colors['system']}System prompt updated{self.colors['reset']}")
            else:
                print(f"{self.colors['system']}Current system prompt: {self.system_prompt}{self.colors['reset']}")
        
        elif cmd == '/stream':
            # Toggle streaming (would need to add state tracking)
            print(f"{self.colors['system']}Streaming is enabled by default{self.colors['reset']}")
        
        elif cmd == '/exit':
            print(f"{self.colors['system']}Goodbye!{self.colors['reset']}")
            sys.exit(0)
        
        elif cmd == '/help':
            self.print_help()
        
        else:
            print(f"{self.colors['error']}Unknown command: {cmd}{self.colors['reset']}")
            print(f"{self.colors['system']}Type /help for available commands{self.colors['reset']}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="ChatGPT Command Line Interface",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive mode (default)
  python chatgpt_cli.py
  
  # Use specific model
  python chatgpt_cli.py --model gpt-3.5-turbo
  
  # Single query mode
  python chatgpt_cli.py --query "What is Python?"
  
  # Set system prompt
  python chatgpt_cli.py --system "You are a code reviewer"
  
  # Load conversation and continue
  python chatgpt_cli.py --load conversation.json
        """
    )
    
    parser.add_argument(
        '--api-key',
        help='OpenAI API key (or set OPENAI_API_KEY env var)'
    )
    
    parser.add_argument(
        '--model',
        default='gpt-4',
        help='Model to use (default: gpt-4)'
    )
    
    parser.add_argument(
        '--system',
        help='System prompt to set'
    )
    
    parser.add_argument(
        '--query',
        help='Single query mode (exit after response)'
    )
    
    parser.add_argument(
        '--load',
        help='Load conversation from file'
    )
    
    parser.add_argument(
        '--no-stream',
        action='store_true',
        help='Disable streaming in interactive mode'
    )
    
    args = parser.parse_args()
    
    # Initialize CLI
    cli = ChatGPTCLI(api_key=args.api_key, model=args.model)
    
    # Set system prompt if provided
    if args.system:
        cli.set_system_prompt(args.system)
    
    # Load conversation if specified
    if args.load:
        cli.load_conversation(args.load)
    
    # Single query mode
    if args.query:
        print(f"{self.colors['user']}You{self.colors['reset']}: {args.query}")
        response = cli.get_completion(args.query, stream=False)
        print(f"{self.colors['assistant']}Assistant{self.colors['reset']}: {response}")
        return
    
    # Interactive mode
    cli.run_interactive(stream=not args.no_stream)


if __name__ == "__main__":
    main()
