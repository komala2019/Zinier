import os

def generate_documentation_html():
    md_path = "B2B_PM_Case_Study_Complete_Deliverable.md"
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Escape any backticks or script tags if needed for raw template embedding
    escaped_md = md_content.replace("</script>", "<\\/script>")

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>B2B PM Case Study: Subcontractor Operations Platform</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <style>
    /* GitHub / Modern Documentation Typography */
    .prose h1 {{ font-size: 2rem; font-weight: 800; border-bottom: 2px solid #334155; padding-bottom: 0.5rem; margin-top: 2rem; margin-bottom: 1rem; color: #f8fafc; }}
    .prose h2 {{ font-size: 1.5rem; font-weight: 700; border-bottom: 1px solid #334155; padding-bottom: 0.4rem; margin-top: 1.8rem; margin-bottom: 0.8rem; color: #38bdf8; }}
    .prose h3 {{ font-size: 1.25rem; font-weight: 600; margin-top: 1.4rem; margin-bottom: 0.6rem; color: #93c5fd; }}
    .prose h4 {{ font-size: 1.05rem; font-weight: 600; margin-top: 1.2rem; margin-bottom: 0.4rem; color: #e2e8f0; }}
    .prose p {{ line-height: 1.7; margin-bottom: 1rem; color: #cbd5e1; }}
    .prose ul, .prose ol {{ margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.7; color: #cbd5e1; }}
    .prose ul {{ list-style-type: disc; }}
    .prose ol {{ list-style-type: decimal; }}
    .prose li {{ margin-bottom: 0.35rem; }}
    .prose blockquote {{ border-left: 4px solid #3b82f6; padding-left: 1rem; margin: 1.2rem 0; font-style: italic; color: #94a3b8; background: rgba(30, 41, 59, 0.4); border-radius: 0 0.5rem 0.5rem 0; padding-top: 0.5rem; padding-bottom: 0.5rem; }}
    .prose table {{ width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.875rem; }}
    .prose th {{ background-color: #1e293b; color: #f8fafc; text-align: left; padding: 0.75rem 1rem; border: 1px solid #334155; font-weight: 700; }}
    .prose td {{ padding: 0.65rem 1rem; border: 1px solid #334155; color: #cbd5e1; }}
    .prose tr:nth-child(even) {{ background-color: rgba(30, 41, 59, 0.3); }}
    .prose code {{ background-color: #1e293b; color: #38bdf8; padding: 0.2rem 0.4rem; border-radius: 0.25rem; font-family: monospace; font-size: 0.875em; }}
    .prose pre {{ background-color: #0b1120; border: 1px solid #334155; border-radius: 0.75rem; padding: 1rem; overflow-x: auto; margin: 1.2rem 0; }}
    .prose pre code {{ background-color: transparent; color: #e2e8f0; padding: 0; }}
    .prose a {{ color: #60a5fa; text-decoration: underline; text-underline-offset: 3px; }}
    .prose a:hover {{ color: #93c5fd; }}
    .prose hr {{ border-color: #334155; margin: 2rem 0; }}
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col antialiased">

  <!-- Top Header Navigation -->
  <header class="sticky top-0 z-50 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 px-6 py-3.5">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-3">
      <div class="flex items-center gap-3">
        <a href="index.html" class="flex items-center gap-2 text-white hover:text-blue-400 transition-colors">
          <span class="px-2.5 py-1 text-xs font-bold rounded-lg bg-blue-600 text-white uppercase tracking-wider">Zinier B2B PM</span>
          <span class="font-extrabold text-sm sm:text-base">Subcontractor Operations Platform</span>
        </a>
      </div>

      <nav class="flex items-center gap-2">
        <a href="index.html" class="px-3 py-1.5 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 transition-colors">
          Overview
        </a>
        <a href="wireframes.html" class="px-3 py-1.5 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 transition-colors flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5 text-blue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
          Wireframes
        </a>
        <a href="presentation_deck.html" class="px-3 py-1.5 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700 transition-colors flex items-center gap-1.5">
          <svg class="w-3.5 h-3.5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"/></svg>
          Slide Deck
        </a>
        <a href="presentation_deck.pptx" download class="px-3 py-1.5 text-xs font-semibold rounded-lg bg-blue-600 text-white hover:bg-blue-500 transition-colors flex items-center gap-1.5 shadow-sm">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
          Download PPTX
        </a>
      </nav>
    </div>
  </header>

  <!-- Main Content Layout -->
  <div class="max-w-7xl w-full mx-auto px-4 sm:px-6 py-8 flex-1 flex flex-col lg:flex-row gap-8">
    
    <!-- Table of Contents Sidebar -->
    <aside class="w-full lg:w-72 flex-shrink-0">
      <div class="sticky top-20 bg-slate-900/80 p-5 rounded-2xl border border-slate-800 space-y-3">
        <h3 class="text-xs font-bold uppercase tracking-wider text-slate-400">Navigation & Jump Links</h3>
        <ul class="text-xs space-y-2 text-slate-300">
          <li><a href="#1-executive-summary--product-positioning" class="hover:text-cyan-400 transition-colors">1. Executive Summary & Positioning</a></li>
          <li><a href="#2-task-1-deep-product-discovery-assumptions--persona-qa" class="hover:text-cyan-400 transition-colors">2. Product Discovery & Personas</a></li>
          <li><a href="#21-core-foundational-assumptions-matrix" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• Assumptions Matrix</a></li>
          <li><a href="#22-persona-1-operator-regional-manager-priya-sharma" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• Persona: Regional Ops</a></li>
          <li><a href="#23-persona-2-operator-vendor-manager-david-vance" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• Persona: Vendor Commercials</a></li>
          <li><a href="#24-persona-3-subcontractor-owner--dispatcher-imran-khan--meera" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• Persona: Subcontractor Owner</a></li>
          <li><a href="#25-persona-4-field-technician-ravi-patel" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• Persona: Field Technician</a></li>
          <li><a href="#3-task-2-live-presentation-content-sections-21--28" class="hover:text-cyan-400 transition-colors">3. Presentation Deliverables (2.1 - 2.8)</a></li>
          <li><a href="#21-field-technician-mobile-app--onboarding-ux-architecture" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• 2.1 Mobile App & Onboarding</a></li>
          <li><a href="#22-operator-performance-management--request-resolution-console" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• 2.2 Operator Console</a></li>
          <li><a href="#23-api--system-architecture-operator-sor-3rd-party-degraded-modes" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• 2.3 System & API Architecture</a></li>
          <li><a href="#24-ai-workflow-deep-dive-smart-evidence-verification--scope-triage" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• 2.4 AI Workflow Deep-Dive</a></li>
          <li><a href="#25-implementation-challenges-technical-adoption-commercial" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• 2.5 Implementation Challenges</a></li>
          <li><a href="#26-business-models-unit-economics--margin-preservation" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• 2.6 Economics & 2.86x ROI</a></li>
          <li><a href="#27-go-to-market-gtm-strategy-scaling-from-signature-to-200-firms" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• 2.7 4-Phase GTM Strategy</a></li>
          <li><a href="#28-strategic-roadmap--horizon-23-improvements" class="pl-3 block text-slate-400 hover:text-cyan-400 transition-colors">• 2.8 18-Month Strategic Roadmap</a></li>
          <li><a href="#4-task-3-roleplay--the-coo-executive-pitch" class="hover:text-cyan-400 transition-colors">4. Task 3: The COO Executive Pitch</a></li>
          <li><a href="#5-task-4-roleplay--scathing-self-critique--defensive-teardown" class="hover:text-cyan-400 transition-colors">5. Task 4: Scathing Critique & Defense</a></li>
        </ul>
      </div>
    </aside>

    <!-- Main Document Article -->
    <main class="flex-1 bg-slate-900/60 p-6 sm:p-10 rounded-2xl border border-slate-800 shadow-xl overflow-hidden">
      <article id="docRender" class="prose max-w-none">
        <!-- Rendered by Marked.js -->
      </article>
    </main>

  </div>

  <!-- Raw Markdown Data Script -->
  <script type="text/markdown" id="rawMarkdown">
{escaped_md}
  </script>

  <script>
    document.addEventListener("DOMContentLoaded", function() {{
      mermaid.initialize({{ startOnLoad: false, theme: 'dark' }});
      
      const rawText = document.getElementById("rawMarkdown").textContent.trim();
      
      // Custom renderer for marked to support mermaid blocks
      const renderer = new marked.Renderer();
      const defaultCodeRenderer = renderer.code.bind(renderer);
      
      renderer.code = function(code, language) {{
        if (language === 'mermaid') {{
          return '<div class="mermaid my-6 p-4 bg-slate-900 rounded-xl border border-slate-800 text-center">' + code + '</div>';
        }}
        return defaultCodeRenderer(code, language);
      }};

      marked.setOptions({{
        renderer: renderer,
        gfm: true,
        breaks: false
      }});

      document.getElementById("docRender").innerHTML = marked.parse(rawText);
      mermaid.init(undefined, document.querySelectorAll('.mermaid'));
    }});
  </script>
</body>
</html>
"""

    with open("documentation.html", "w", encoding="utf-8") as f:
        f.write(html_template)
    print("documentation.html generated successfully.")

if __name__ == "__main__":
    generate_documentation_html()
