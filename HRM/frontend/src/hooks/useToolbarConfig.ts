import { useState, useEffect } from 'react';

export interface ToolbarPermissions {
  new: boolean;
  edit: boolean;
  refresh: boolean;
  search: boolean;
  filter: boolean;
  exit: boolean;
  view: boolean;
  delete: boolean;
  import: boolean;
  export: boolean;
  clone: boolean;
  notes: boolean;
  attach: boolean;
  help: boolean;
  save: boolean;
  cancel: boolean;
  clear: boolean;
  authorize: boolean;
  submit: boolean;
  reject: boolean;
  amend: boolean;
  print: boolean;
  email: boolean;
  first: boolean;
  prev: boolean;
  next: boolean;
  last: boolean;
  hold: boolean;
  void: boolean;
}

interface ToolbarConfigResponse {
  permissions: ToolbarPermissions;
  config: string;
}

// ERP Menu Item toolbar configuration (from database)
// This should be loaded from the ERP Menu Item table
const ERP_MENU_ITEMS: Record<string, {
  toolbar_list: string;
  toolbar_view: string;
  toolbar_edit: string;
  toolbar_create: string;
}> = {
  'EMPLOYEE_RECORDS': {
    toolbar_list: 'NRQFVEDIOX',
    toolbar_view: 'X',
    toolbar_edit: 'SCX',
    toolbar_create: 'SCX',
  },
  'HRM_ORG_CHART': {
    toolbar_list: 'NRQFVIOX',
    toolbar_view: 'X',
    toolbar_edit: 'SCX',
    toolbar_create: 'SCX',
  },
  'HRM_PROFILE_VIEW': {
    toolbar_list: 'NRQFVIOX',
    toolbar_view: 'X',
    toolbar_edit: 'SCX',
    toolbar_create: 'SCX',
  },
  'HRM_DOCUMENT_MANAGEMENT': {
    toolbar_list: 'NESCKVDXRQF',
    toolbar_view: 'X',
    toolbar_edit: 'SCX',
    toolbar_create: 'SCX',
  },
  'HRM_EMPLOYEE_SELF_SERVICE': {
    toolbar_list: 'NESCKVDXRQF',
    toolbar_view: 'X',
    toolbar_edit: 'SCX',
    toolbar_create: 'SCX',
  },
  'HRM_EMPLOYEE_LIFECYCLE': {
    toolbar_list: 'NESCKVDXRQF',
    toolbar_view: 'X',
    toolbar_edit: 'SCX',
    toolbar_create: 'SCX',
  },
};

// Helper function to convert character string to permissions object
const parseConfigString = (configString: string): ToolbarPermissions => {
  const permissions: ToolbarPermissions = {
    new: false,
    edit: false,
    refresh: false,
    search: false,
    filter: false,
    exit: false,
    view: false,
    delete: false,
    import: false,
    export: false,
    clone: false,
    notes: false,
    attach: false,
    help: false,
    save: false,
    cancel: false,
    clear: false,
    authorize: false,
    submit: false,
    reject: false,
    amend: false,
    print: false,
    email: false,
    first: false,
    prev: false,
    next: false,
    last: false,
    hold: false,
    void: false,
  };

  const actionMap: Record<string, keyof ToolbarPermissions> = {
    'N': 'new',
    'E': 'edit',
    'R': 'refresh',
    'Q': 'search',
    'F': 'filter',
    'X': 'exit',
    'V': 'view',
    'D': 'delete',
    'I': 'import',
    'O': 'export',
    'L': 'clone',
    'B': 'notes',
    'U': 'attach',
    'G': 'help',
    'S': 'save',
    'C': 'cancel',
    'K': 'clear',
    'A': 'authorize',
    'T': 'submit',
    'J': 'reject',
    'W': 'amend',
    'P': 'print',
    'M': 'email',
    '1': 'first',
    '2': 'prev',
    '3': 'next',
    '4': 'last',
    'H': 'hold',
    'Z': 'void',
  };

  for (const char of configString.toUpperCase()) {
    if (actionMap[char]) {
      permissions[actionMap[char]] = true;
    }
  }

  return permissions;
};

export const useToolbarConfig = (viewId: string, mode: string = 'LIST') => {
  const [config, setConfig] = useState<ToolbarConfigResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadToolbarConfig = () => {
      try {
        setLoading(true);

        // Get the menu item from ERP Menu Item configuration
        const menuItem = ERP_MENU_ITEMS[viewId];

        if (!menuItem) {
          console.warn(`Menu item not found: ${viewId}`);
          setConfig(null);
          setLoading(false);
          return;
        }

        // Get mode-specific toolbar configuration
        const modeColumn = `toolbar_${mode.toLowerCase()}` as keyof typeof menuItem;
        const toolbarConfig = menuItem[modeColumn] || '';

        // Parse the character string to permissions
        const permissions = parseConfigString(toolbarConfig);

        setConfig({
          permissions,
          config: toolbarConfig,
        });
      } catch (error) {
        console.error('Failed to load toolbar config:', error);
        setConfig(null);
      } finally {
        setLoading(false);
      }
    };

    loadToolbarConfig();
  }, [viewId, mode]);

  return { config, loading };
};

// Export the new useToolbarPermissions hook for API-driven system
export const useToolbarPermissions = (viewId: string, mode: string, skip: boolean = false) => {
  const [allowedActions, setAllowedActions] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (skip) {
      setLoading(false);
      return;
    }

    const loadPermissions = () => {
      try {
        setLoading(true);
        setError(null);

        // Get the menu item from ERP Menu Item configuration
        const menuItem = ERP_MENU_ITEMS[viewId];

        if (!menuItem) {
          setError(`Menu item not found: ${viewId}`);
          setLoading(false);
          return;
        }

        // Get mode-specific toolbar configuration
        const modeColumn = `toolbar_${mode.toLowerCase()}` as keyof typeof menuItem;
        const toolbarConfig = menuItem[modeColumn] || '';

        // Parse the character string to action IDs
        const actionMap: Record<string, string> = {
          'N': 'new',
          'E': 'edit',
          'R': 'refresh',
          'Q': 'search',
          'F': 'filter',
          'X': 'exit',
          'V': 'view',
          'D': 'delete',
          'I': 'import',
          'O': 'export',
          'L': 'clone',
          'B': 'notes',
          'U': 'attach',
          'G': 'help',
          'S': 'save',
          'C': 'cancel',
          'K': 'clear',
          'A': 'authorize',
          'T': 'submit',
          'J': 'reject',
          'W': 'amend',
          'P': 'print',
          'M': 'email',
          '1': 'first',
          '2': 'prev',
          '3': 'next',
          '4': 'last',
          'H': 'hold',
          'Z': 'void',
        };

        const actions: string[] = [];
        for (const char of toolbarConfig.toUpperCase()) {
          if (actionMap[char]) {
            actions.push(actionMap[char]);
          }
        }

        setAllowedActions(actions);
        setLoading(false);
      } catch (err) {
        setError('Failed to load toolbar permissions');
        setLoading(false);
      }
    };

    loadPermissions();
  }, [viewId, mode, skip]);

  return { allowedActions, loading, error };
};
