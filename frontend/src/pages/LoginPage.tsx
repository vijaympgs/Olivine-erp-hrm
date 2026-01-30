import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../auth/useAuth";
import { Button } from "@ui/Button";
import { Input } from "@ui/Input";
import { companyService, CompanyListItem } from "@services/companyService";
import { LocationSelectionModal } from "@ui/LocationSelectionModal";
import { LocationListItem } from "@services/locationService";
import { Building, ArrowRight, ShieldCheck } from "lucide-react";
import { PlatformVersionModal } from "../components/PlatformVersionModal";


export const LoginPage: React.FC = () => {
  const { login, isLoading: authLoading } = useAuth();
  const navigate = useNavigate();

  const [username, setUsername] = useState("admin");
  const [password, setPassword] = useState("admin123");
  const [rememberMe, setRememberMe] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  // Company Selection
  const [companies, setCompanies] = useState<CompanyListItem[]>([]);
  const [selectedCompanyId, setSelectedCompanyId] = useState("");
  const [loadingCompanies, setLoadingCompanies] = useState(true);

  // Location Selection Modal
  const [showLocationModal, setShowLocationModal] = useState(false);
  const [loginSuccess, setLoginSuccess] = useState(false);

  // Platform Version Modal
  const [showVersionModal, setShowVersionModal] = useState(false);

  useEffect(() => {
    const fetchCompanies = async () => {
      try {
        setLoadingCompanies(true);
        const list = await companyService.getActiveCompanies();
        console.log('Fetched companies:', list);
        if (list && list.length > 0) {
          setCompanies(list);
          setSelectedCompanyId(list[0].id);
        } else {
          // No companies found - show message
          console.warn("No active companies found in database");
          setCompanies([]);
          setError("No companies configured. Please contact administrator.");
        }
      } catch (err) {
        console.error("Failed to fetch companies:", err);
        setError("Failed to load companies. Please check backend connection.");
        setCompanies([]);
      } finally {
        setLoadingCompanies(false);
      }
    };
    fetchCompanies();
  }, []);

  // Keyboard shortcut: Ctrl+L to show version info
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.ctrlKey && e.key === 'l') {
        e.preventDefault();
        setShowVersionModal(prev => !prev);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSubmitting(true);
    try {
      await login({
        username,
        password,
        rememberMe,
        companyId: selectedCompanyId
      });

      // Check if location is already selected
      const existingLocation = localStorage.getItem('session_location_id');
      if (existingLocation) {
        // Location already selected, navigate directly
        navigate("/", { replace: true });
      } else {
        // Navigate to dedicated Location Selection page
        navigate("/location-selection", { replace: true });
      }
    } catch (err: any) {
      setError(err?.message ?? "Failed to sign in");
    } finally {
      setSubmitting(false);
    }
  };

  // Modal handler removed as we now redirect


  return (
    // Neutral Background for Contrast
    <div className="fixed inset-0 flex items-center justify-center bg-[#F3F4F6] px-4 z-50 font-sans">

      {/* SHADOW CARD CONTAINER: 50/50 Split - max-w-5xl */}
      <div className="flex w-full max-w-5xl h-[550px] bg-white shadow-2xl rounded-none overflow-hidden border border-gray-100">

        {/* LEFT PANEL: Branding (50%) */}
        <div
          className="hidden md:flex w-1/2 flex-col justify-between p-12 text-white relative bg-gray-900"
          style={{ backgroundImage: "url('/login-bg.png')", backgroundSize: 'cover', backgroundPosition: 'center' }}
        >
          {/* Gradients & Overlays for Depth */}
          <div className="absolute inset-0 bg-gradient-to-b from-purple-900/60 via-purple-900/40 to-black/80 mix-blend-multiply z-0" />
          <div className="absolute inset-0 bg-black/20 z-0" />

          {/* Branding */}
          <div className="relative z-10 space-y-3">
            {/* Signature Orange Bar */}
            <div className="h-8 w-1.5 bg-orange-500 mb-4 rounded-none shadow-[0_0_15px_rgba(249,115,22,0.6)]" />

            <div>
              <h1 className="text-3xl font-bold tracking-tight text-white mb-2">
                Olivine Console
              </h1>
              <p className="text-blue-100/80 text-sm font-light leading-relaxed max-w-sm">
                Orchestrating excellence through unified intelligence.
              </p>
            </div>
          </div>

          {/* Footer Info */}
          <div className="relative z-10 text-[10px] text-white/40 uppercase tracking-widest font-medium grid gap-1">
            <p>System v0.1 • Authorized Access Only</p>
            <p className="font-light normal-case tracking-normal text-white/30">© 2025 Olivine Inc.</p>
          </div>
        </div>

        {/* RIGHT PANEL: Form (50%) */}
        <div className="flex w-full md:w-1/2 flex-col justify-center px-16 py-8 bg-white relative">

          <div className="w-full max-w-sm mx-auto relative z-10">
            <div className="mb-8">
              <h2 className="text-2xl font-bold text-gray-900 tracking-tight text-left">Console Access</h2>
              <p className="text-gray-500 mt-1 text-sm">Verify credentials to establish connection.</p>
            </div>

            <form className="space-y-5" onSubmit={handleSubmit}>

              {/* Company Select */}
              <div className="space-y-1">
                <label className="block text-[10px] font-bold text-gray-400 uppercase tracking-widest font-mono">
                  Target Workspace
                </label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <Building className="h-4 w-4 text-gray-400" />
                  </div>
                  <select
                    value={selectedCompanyId}
                    onChange={(e) => setSelectedCompanyId(e.target.value)}
                    className="block w-full pl-9 pr-8 py-2.5 text-sm bg-gray-50 border border-gray-200 text-gray-900 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent focus:bg-white transition-all rounded-none appearance-none cursor-pointer font-medium hover:bg-gray-100/50"
                    disabled={loadingCompanies}
                  >
                    {loadingCompanies ? (
                      <option>Loading...</option>
                    ) : (
                      companies.map(c => (
                        <option key={c.id} value={c.id}>
                          {c.company_name} ({c.company_code})
                        </option>
                      ))
                    )}
                  </select>
                  <div className="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none text-gray-400">
                    <svg className="h-3 w-3 fill-current" viewBox="0 0 20 20"><path d="M7 10l5 5 5-5H7z" /></svg>
                  </div>
                </div>
              </div>

              {/* Username/Email -> Access ID */}
              <div className="space-y-1">
                <label className="block text-[10px] font-bold text-gray-400 uppercase tracking-widest font-mono">
                  Access ID
                </label>
                <Input
                  type="text"
                  value={username}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) => setUsername(e.target.value)}
                  required
                  placeholder="username or email@olivine.ai"
                  data-testid="username"
                  className="w-full rounded-none border-gray-200 bg-gray-50 py-2.5 text-gray-900 placeholder-gray-400 focus:ring-2 focus:ring-purple-600 focus:border-transparent focus:bg-white transition-all hover:bg-gray-100/50 text-sm"
                />
              </div>

              {/* Password -> Passkey */}
              <div className="space-y-1">
                <div className="flex justify-between items-center mb-1">
                  <label className="block text-[10px] font-bold text-gray-400 uppercase tracking-widest font-mono">
                    Passkey
                  </label>
                  <a href="#" className="text-[10px] font-semibold text-purple-600 hover:text-purple-700 transition-colors">
                    Recovery?
                  </a>
                </div>
                <Input
                  type="password"
                  value={password}
                  onChange={(e: React.ChangeEvent<HTMLInputElement>) => setPassword(e.target.value)}
                  required
                  placeholder="••••••••"
                  data-testid="password"
                  className="w-full rounded-none border-gray-200 bg-gray-50 py-2.5 text-gray-900 placeholder-gray-400 focus:ring-2 focus:ring-purple-600 focus:border-transparent focus:bg-white transition-all hover:bg-gray-100/50 text-sm"
                />
              </div>

              {/* Actions */}
              <div className="pt-1">
                <label className="flex items-center gap-2 text-sm text-gray-600 cursor-pointer group select-none">
                  <div className="relative flex items-center">
                    <input
                      type="checkbox"
                      checked={rememberMe}
                      onChange={e => setRememberMe(e.target.checked)}
                      className="peer h-4 w-4 cursor-pointer appearance-none rounded-none border-2 border-gray-300 transition-all checked:border-purple-600 checked:bg-purple-600 hover:border-purple-400"
                    />
                    <svg className="absolute w-3 h-3 ml-0.5 mt-0.5 hidden peer-checked:block pointer-events-none text-white left-0 top-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="4" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                  </div>
                  <span className="group-hover:text-gray-900 transition-colors font-medium text-xs">Keep session active</span>
                </label>
              </div>

              {error && (
                <div className="rounded-none bg-red-50 border-l-4 border-red-500 p-3">
                  <div className="flex">
                    <div className="flex-shrink-0">
                      <ShieldCheck className="h-4 w-4 text-red-500" />
                    </div>
                    <div className="ml-3">
                      <p className="text-xs text-red-700 font-medium">{error}</p>
                    </div>
                  </div>
                </div>
              )}

              <Button
                type="submit"
                disabled={submitting || authLoading || loadingCompanies}
                data-testid="btn-login"
                className="w-full flex justify-center items-center gap-2 py-3 text-sm font-bold rounded-none text-white bg-gray-900 hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-900 shadow-lg transition-all active:scale-[0.99] uppercase tracking-wide"
              >
                {submitting ? "Verifying..." : "Authenticate Session"}
                {!submitting && <ArrowRight className="w-4 h-4 ml-1" />}
              </Button>

              {/* Platform Version Hint */}
              <div className="mt-4 text-center">
                <p className="text-xs text-gray-400">
                  Press <kbd className="px-1.5 py-0.5 bg-gray-100 border border-gray-300 rounded text-[10px] font-mono">Ctrl</kbd> + <kbd className="px-1.5 py-0.5 bg-gray-100 border border-gray-300 rounded text-[10px] font-mono">L</kbd> for platform info
                </p>
              </div>

            </form>
          </div>

          {/* Decorative Clean Background shape on right side (Scaled) */}
          <div className="absolute top-0 right-0 w-48 h-48 bg-gray-50 rounded-full blur-3xl -translate-y-1/2 translate-x-1/2 opacity-50 pointer-events-none" />
          <div className="absolute bottom-0 left-0 w-32 h-32 bg-purple-50 rounded-full blur-3xl translate-y-1/2 -translate-x-1/2 opacity-50 pointer-events-none" />

        </div>
      </div>

      {/* Platform Version Modal */}
      <PlatformVersionModal
        isOpen={showVersionModal}
        onClose={() => setShowVersionModal(false)}
      />

      {/* Location Selection Modal Removed - Redirects to Page now */}
    </div>
  );
};


