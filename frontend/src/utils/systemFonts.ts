// OS-specific font lists for menu typography
export const WINDOWS_FONTS = [
    'Segoe UI',
    'Arial',
    'Calibri',
    'Consolas',
    'Courier New',
    'Georgia',
    'Tahoma',
    'Times New Roman',
    'Trebuchet MS',
    'Verdana',
];

export const LINUX_FONTS = [
    'Ubuntu',
    'DejaVu Sans',
    'Liberation Sans',
    'Noto Sans',
    'Roboto',
    'Droid Sans',
    'FreeSans',
    'Cantarell',
    'Oxygen',
];

export const UNIVERSAL_FONTS = [
    'Inter',
    'system-ui',
    '-apple-system',
    'sans-serif',
    'monospace',
];

// Detect OS and return appropriate font list
export const getSystemFonts = (): string[] => {
    const userAgent = navigator.userAgent.toLowerCase();

    if (userAgent.includes('win')) {
        return [...WINDOWS_FONTS, ...UNIVERSAL_FONTS];
    } else if (userAgent.includes('linux')) {
        return [...LINUX_FONTS, ...UNIVERSAL_FONTS];
    } else if (userAgent.includes('mac')) {
        return [
            'SF Pro Display',
            'Helvetica Neue',
            'Arial',
            ...UNIVERSAL_FONTS
        ];
    }

    return UNIVERSAL_FONTS;
};
