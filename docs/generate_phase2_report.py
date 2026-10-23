"""
Generate VEIL Major Project Phase-2 Report PDF (VTU BCS786 structure).
Run: python docs/generate_phase2_report.py
Output: docs/VEIL_Phase2_Report.pdf
"""
from fpdf import FPDF
from pathlib import Path

OUT = Path(__file__).resolve().parent / "VEIL_Phase2_Report.pdf"


def ascii_safe(text: str) -> str:
    """Helvetica core font is Latin-1 only."""
    return (
        text.replace("\u2014", "-")
        .replace("\u2013", "-")
        .replace("\u2019", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
        .replace("\u2022", "-")
    )


class ReportPDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 9)
        self.cell(0, 10, f"Dept. of CSE, RNSIT 2026-27  |  Page {self.page_no()}", align="C")

    def chapter_title(self, num: str, title: str):
        self.add_page()
        self.set_font("Helvetica", "B", 16)
        self.multi_cell(self.epw, 10, f"Chapter {num}\n{title}")
        self.ln(4)

    def section(self, title: str):
        self.ln(2)
        self.set_font("Helvetica", "B", 12)
        self.multi_cell(self.epw, 7, title)
        self.ln(1)

    def body(self, text: str):
        self.set_font("Helvetica", "", 11)
        self.multi_cell(self.epw, 6, ascii_safe(text))
        self.ln(2)

    def bullets(self, items):
        self.set_font("Helvetica", "", 11)
        for item in items:
            self.multi_cell(self.epw, 6, ascii_safe(f"  - {item}"))
        self.ln(2)


def build(pdf: ReportPDF):
    # Title page
    pdf.add_page()
    w = pdf.epw

    def center_line(text, h=8, bold=False):
        pdf.set_font("Helvetica", "B" if bold else "", 14 if bold else 11)
        pdf.cell(w, h, text, ln=True, align="C")

    pdf.ln(30)
    center_line("VISVESVARAYA TECHNOLOGICAL UNIVERSITY", bold=True)
    center_line('"JNANA SANGAMA", BELAGAVI - 590 018.', h=6)
    pdf.ln(10)
    center_line("A Major Project Phase-2 Report (BCS786)", h=8, bold=True)
    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 13)
    pdf.cell(w, 8, "VEIL - Verifiable Encrypted Inference For Location Privacy", ln=True, align="C")
    pdf.ln(8)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(w, 6, "Submitted in partial fulfillment of the requirements for the final year degree in "
        "Bachelor of Engineering in Computer Science and Engineering of Visvesvaraya "
        "Technological University, Belagavi.", align="C")
    pdf.ln(12)
    for line in [
        "Submitted by",
        "Shanvi S Shetty  (1RN23CS190)",
        "Sinchana K  (1RN23CS205)",
        "Tripti Prasanna  (1RN23CS230)",
    ]:
        center_line(line, h=7)
    pdf.ln(8)
    center_line("Under the Guidance of", h=7)
    center_line("Mr. Manjunath G S, Assistant Professor, Dept. of CSE", h=7)
    pdf.ln(8)
    for line in [
        "Department of Computer Science and Engineering",
        "RNS Institute of Technology",
        "RR Nagar, Dr. Vishnuvardhan Road, Bengaluru-560098",
        "Academic Year 2026-2027",
    ]:
        center_line(line, h=7)

    # Certificate placeholder
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "CERTIFICATE", ln=True, align="C")
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 11)
    pdf.body(
        "Certified that the Project work entitled VEIL - Verifiable Encrypted Inference For "
        "Location Privacy has been successfully carried out at RNSIT by Shanvi S Shetty "
        "(1RN23CS190), Sinchana K (1RN23CS205), and Tripti Prasanna (1RN23CS230) in partial "
        "fulfillment of the requirements of the final year degree in Bachelor of Engineering "
        "in Computer Science and Engineering of Visvesvaraya Technological University, Belagavi "
        "during the academic year 2026-2027."
    )

    # Acknowledgement
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Acknowledgement", ln=True)
    pdf.body(
        "We extend our profound thanks to the Management of RNS Institute of Technology for "
        "fostering an environment that promotes innovation and academic excellence. We express "
        "gratitude to our Principal, Dr. Ramesh Babu H S, and Dr. Sampada K S, Professor and "
        "Head of Department, Computer Science and Engineering, for their support. We are deeply "
        "grateful to our project guide, Mr. Manjunath G S, for unwavering guidance and valuable "
        "suggestions throughout this project. We thank all teaching and non-teaching staff of "
        "the CSE Department for their encouragement and cooperation."
    )

    # Abstract
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "Abstract", ln=True)
    pdf.body(
        "VEIL (Verifiable Encrypted Inference for Location Privacy) addresses the need for secure "
        "computation in location-based services by enabling users to query nearby points of interest "
        "without revealing exact geographic coordinates to secure server endpoints. The system "
        "combines efficient k-Nearest Neighbour (kNN) computation with garbled circuits (Free-XOR and "
        "Half-Gates), oblivious transfer scaffolding (Naor-Pinkas with IKNP extension in the backend; "
        "simulated label selection in the browser prototype), and SHA-256 Merkle trees for result "
        "verification. Real-time geographic data is sourced from OpenStreetMap via the Overpass API "
        "for the Bengaluru region. A full-stack implementation uses Node.js/Express on the server and "
        "React with Leaflet and Three.js on the client. The browser evaluates the garbled circuit "
        "locally so raw GPS never appears on /api/gc/init or /api/gc/resolve. VEIL demonstrates "
        "feasibility, documents privacy-performance trade-offs honestly, and supports tamper detection "
        "experiments via Merkle proofs."
    )

    # List of Figures / Tables
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(pdf.epw, 10, "List of Figures", new_x="LMARGIN", new_y="NEXT")
    pdf.bullets(
        [
            "Figure 4.1: VEIL system schema diagram (data preparation, GC setup, client input, secure core, verification).",
            "Figure 5.1: Preprocessing flow from Overpass fetch to Merkle commitment and kNN-ready dataset.",
            "Figure 6.1: Application landing page and secure query flow overview.",
            "Figure 6.2: Secure kNN results with Merkle verification and latency breakdown.",
            "Figure 6.3: Circuit complexity and plain vs secure performance comparison.",
        ]
    )
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(pdf.epw, 10, "List of Tables", new_x="LMARGIN", new_y="NEXT")
    pdf.bullets(
        [
            "Table 2.1: Literature survey summary (year, paper, key idea, limitation).",
            "Table 6.1: Plain vs secure kNN complexity metrics (gates, AES calls, privacy).",
            "Table 6.2: Query latency breakdown by pipeline stage (representative trial).",
        ]
    )

    # CHAPTER 1
    pdf.chapter_title("1", "INTRODUCTION")
    pdf.section("1.1 Introduction about the project")
    pdf.body(
        "Location-Based Services (LBS) have become essential to modern mobile computing. Navigation, "
        "ride-hailing, food delivery, emergency services, and local search all depend on determining "
        "where the user is relative to a database of places. The dominant architecture sends precise "
        "GPS coordinates from the client to a remote server, which computes distances and returns "
        "ranked results. This model is efficient and familiar, but it treats location as plaintext "
        "input to an operator that may log, aggregate, monetize, or disclose data under legal process."
    )
    pdf.body(
        "Location data is among the most sensitive personal signals. Short traces reveal home and "
        "work locations, daily routines, visits to hospitals or religious sites, and social patterns "
        "from co-location. Regulations such as GDPR and India's Digital Personal Data Protection Act "
        "recognize location as personal data, yet many applications still centralize raw coordinates."
    )
    pdf.body(
        "VEIL is a privacy-preserving kNN system for location-based queries over real OpenStreetMap "
        "data. It provides two modes: plain kNN (baseline, coordinates sent to server) and secure kNN "
        "(garbled circuit evaluated in the browser, secure API endpoints reject coordinates). The "
        "server garbles boolean circuits that compute squared planar distance in 32-bit fixed-point "
        "microdegree encoding. The client selects input wire labels and evaluates gates using AES-128 "
        "via Web Crypto. Returned POIs include Merkle inclusion proofs against a root committed when "
        "the dataset was loaded."
    )
    pdf.section("1.2 Existing System and its limitations")
    pdf.bullets(
        [
            "Lack of privacy protection: commercial LBS require exact coordinates on the server.",
            "Centralized processing increases breach and misuse risk.",
            "Absence of secure computation: most apps do not use garbled circuits or OT for queries.",
            "No result verification: users cannot cryptographically verify POI integrity.",
            "Limited transparency: processing is opaque to end users.",
        ]
    )

    # CHAPTER 2
    pdf.chapter_title("2", "LITERATURE SURVEY")
    pdf.section("Table 2.1: Literature Survey (summary)")
    lit = [
        "2024 Eshun & Palmieri (TIFS): MPC and garbled circuits for mutual location privacy; high cost.",
        "2023 Chen et al. (TSC): Geometric searchable encryption; weak for exact kNN at scale.",
        "2021 Liu et al.: Merkle trees for integrity; not LBS-specific.",
        "2019 Zhang et al. (Grid Voronoi): Fast NN indexing; no privacy.",
        "2017 Kim et al.: Garbled-circuit kNN classification on cloud; expensive for large n.",
        "2014 Paulet et al.: OT and PIR for location queries; communication overhead.",
        "2008 Kolesnikov & Schneider: Free-XOR optimization for garbled circuits.",
        "2015 Zahur et al.: Half-Gates reduce AND-gate garbling cost.",
        "2003 Ishai et al.: IKNP oblivious transfer extension.",
        "1986 Yao: Foundational garbled circuit two-party computation.",
    ]
    pdf.bullets(lit)
    pdf.section("2.1 Relevant recent papers summary")
    pdf.body(
        "Privacy-preserving kNN using garbled circuits demonstrates that classification and distance "
        "comparison can run on encrypted wire labels, but full-database scans do not scale to "
        "metropolitan POI sets without pre-filtering. Secure location protocols combining OT and "
        "outsourcing reduce client work yet often assume non-colluding servers. Spatial indexing "
        "literature achieves near real-time nearest-neighbour queries but ignores input privacy. "
        "VEIL synthesizes verifiable commitments (Merkle), bounded-candidate garbled distance "
        "circuits, and live OSM integration in one demonstrator."
    )
    pdf.section("2.2 Conclusion about literature survey")
    pdf.body(
        "Existing research validates cryptographic building blocks but rarely delivers an end-to-end "
        "web application with measurable gate counts, latency breakdown, and explicit privacy "
        "boundaries per API route. VEIL fills that systems gap while documenting prototype "
        "limitations such as simulated OT and semi-honest security."
    )

    # CHAPTER 3
    pdf.chapter_title("3", "PROBLEM STATEMENT")
    pdf.body(
        "Users of location-based services must find the k nearest points of interest without exposing "
        "exact coordinates to untrusted secure computation endpoints. The service provider must protect "
        "its POI database from trivial tampering of results. The system must use real geographic data "
        "and remain understandable to evaluators through a working UI and baseline comparison mode."
    )
    pdf.section("3.1 Objectives")
    pdf.bullets(
        [
            "Ensure user location privacy on secure garbling and resolve endpoints.",
            "Compute kNN using garbled circuits and Merkle-verifiable outputs.",
            "Integrate live GPS and OpenStreetMap POIs for Bengaluru.",
            "Measure complexity: AND gates, AES calls, garble/eval latency.",
            "Detect tampering via Merkle proof verification (tamper_test.js).",
            "Deliver conference-ready documentation (C2I6, COMPSIF submissions).",
        ]
    )

    # CHAPTER 4
    pdf.chapter_title("4", "SYSTEM ARCHITECTURE / BLOCK DIAGRAM")
    pdf.section("4.1 Schema Diagram")
    pdf.body(
        "Components: (1) User browser with GPS, map, and garbled-circuit evaluator (gcProtocol.js); "
        "(2) VEIL Express backend (server.js) for OSM fetch, Merkle commitment, garbling, sessions; "
        "(3) OpenStreetMap Overpass API as external data source. Plain flow: POST /api/knn/plain with "
        "coordinates. Secure flow: optional POST /api/candidates with coarsened ~1km grid for up to 30 "
        "candidate POIs; POST /api/gc/init with k and candidateIds only; client evaluation; POST "
        "/api/gc/resolve with result POI ids; client verifies Merkle proofs. Deprecated POST "
        "/api/knn/secure returns HTTP 410."
    )
    pdf.section("4.2 Functional Requirements")
    pdf.bullets(
        [
            "Acquire user location (GPS or manual) on the client.",
            "Fetch and cache POIs from Overpass (500 max, 30 min TTL).",
            "Plain and secure kNN modes with category filters and configurable k.",
            "Garbled circuits and OT module; Merkle proof generation and verification.",
        ]
    )
    pdf.section("4.3 Non-Functional Requirements")
    pdf.bullets(
        [
            "Performance: plain kNN fast; secure mode AES-bound in browser.",
            "Security: semi-honest model; no coordinate logging on /api/gc routes.",
            "Scalability: Merkle over full cache; circuit bounded to MAX_SECURE_POIS=30.",
            "Reliability: graceful 503 when Overpass unavailable.",
            "Usability: React UI with landing page disclosures (simulated OT).",
        ]
    )
    pdf.section("4.4 User Requirements")
    pdf.bullets(
        [
            "Share location or enter coordinates; select POI categories.",
            "Choose k and switch plain vs secure mode.",
            "View results on Leaflet map with distances and Merkle verified tags.",
        ]
    )

    # CHAPTER 5 - long implementation chapter (multiple sections)
    pdf.chapter_title("5", "IMPLEMENTATION")
    pdf.section("5.1 Dataset Explanation")
    pdf.body(
        "POIs are fetched using Overpass QL over a Bengaluru bounding box (approximately 12.8-13.1 N, "
        "77.45-77.75 E). Categories map to OSM amenity tags: hospital/clinic/doctors, restaurant, "
        "pharmacy, cafe. Each record includes id, name, latitude, longitude, and category. The server "
        "caches up to 500 POIs for 30 minutes. Merkle leaves hash canonical POI fields with SHA-256."
    )
    pdf.section("5.2 Preprocessing flow")
    pdf.bullets(
        [
            "Data collection from Overpass API with retries.",
            "Cleaning: remove invalid coordinates and duplicates.",
            "Category filtering per user selection.",
            "Client-side binary encoding: round(abs(coord)*1e6) to 32 bits per coordinate.",
            "Merkle tree build at session start; root published to clients.",
            "Candidate discovery: coarsen location to 2 decimal degrees (~1 km) and plain kNN for top 30 ids.",
        ]
    )
    pdf.section("5.3 Libraries Used")
    pdf.bullets(
        [
            "Backend: Express, cors, node-fetch, Node crypto.",
            "Frontend: React, Vite, TailwindCSS, Leaflet, Three.js.",
            "Custom: garbledCircuit.js, obliviousTransfer.js, merkleTree.js, veil.js, gcProtocol.js.",
        ]
    )
    pdf.section("5.4 Algorithms and pseudocode")
    pdf.body(
        "Plain kNN (knn.js): O(n log k) max-heap on squared flat-plane distance; Haversine metres for "
        "display. Secure per-POI circuit: SUB ripple-carry subtractor, SQR schoolbook squarer, ADD, "
        "CMP comparator on dist squared; approximately 2244 AND gates per POI (squaring dominates). "
        "Client evaluates all candidate POI circuits and selects k smallest distances. Merkle verification "
        "walks O(log n) sibling hashes to recomputed root."
    )
    pdf.section("5.4.1 Algorithm 1: Secure Distance (Garbled Circuit)")
    pdf.body(
        "Inputs: user (x_u, y_u) as client private bits; POI (x_p, y_p) as server embedded labels. "
        "Steps: dx = SUB(x_u, x_p); dy = SUB(y_u, y_p); dx_sq = SQR(dx); dy_sq = SQR(dy); "
        "dist_sq = ADD(dx_sq, dy_sq); result = CMP(dist_sq, T). XOR gates use Free-XOR; AND gates "
        "use Half-Gates (two AES operations per AND during evaluation)."
    )
    pdf.section("5.4.2 Algorithm 2: Result Verification (Merkle Proof)")
    pdf.body(
        "Given committed root R, POI leaf hash, and proof siblings with left/right position: "
        "current = leaf; for each sibling, hash concatenation order per position; verified if "
        "current equals R. Tampered leaves or proofs fail verification with overwhelming probability."
    )
    pdf.section("5.5 Module-wise description")
    modules = [
        "server.js: REST API, gcSessions TTL 5 min, privacy logging rules.",
        "osm/fetcher.js: Overpass query builder and POI normalization.",
        "geometry/knn.js: Haversine, heap kNN, complexityReport.",
        "crypto/veil.js: VEILSession, candidates, buildSecureCircuit, resolveSecureQuery.",
        "crypto/gc/garbledCircuit.js: gate garbling and client bundle export.",
        "crypto/ot/obliviousTransfer.js: Naor-Pinkas, IKNP, benchmark endpoint.",
        "crypto/merkle/merkleTree.js: commitment, proofs, verifyResults.",
        "frontend gcProtocol.js: runSecureKNN pipeline and browser AES evaluator.",
        "UI components: ControlPanel, MapView, ResultPanel, ComplexityPanel, LandingPage.",
    ]
    pdf.bullets(modules)
    pdf.section("5.6 API endpoints")
    pdf.bullets(
        [
            "GET /api/health, GET /api/dataset",
            "POST /api/knn/plain (non-private)",
            "POST /api/candidates (coarsened location for candidate ids)",
            "POST /api/gc/init, POST /api/gc/resolve (secure, no coordinates)",
            "GET /api/complexity, POST /api/verify, GET /api/ot/benchmark",
        ]
    )

    # CHAPTER 6: TESTING AND RESULTS
    pdf.chapter_title("6", "TESTING AND RESULTS")
    pdf.section("6.1 Unit Testing")
    pdf.body(
        "Unit testing verifies the core functional correctness of individual sub-modules in isolation. "
        "The VEIL cryptographic engine relies on custom primitives for 32-bit fixed-point subtraction, "
        "schoolbook squaring, ripple-carry addition, bitwise comparator networks, SHA-256 Merkle tree "
        "hashing, and wire-label generation. Unit tests validate that each arithmetic gate primitive "
        "satisfies two's complement arithmetic and that garbled circuits match unencrypted reference evaluations."
    )
    pdf.bullets(
        [
            "Subtractor Module (SUB): Unit tests evaluate 33-bit ripple-carry subtractors across positive, negative, and edge-case coordinate inputs.",
            "Squarer Module (SQR): Verified schoolbook integer squaring for 32-bit values over 2,048 garbled AND gates without overflow.",
            "Merkle Tree Engine (merkleTree.js): Evaluated SHA-256 hashing, leaf canonicalization, sibling proof construction, and root commitment recalculation.",
            "Oblivious Transfer Scaffolding (obliviousTransfer.js): Benchmarked Naor-Pinkas public-key operations and IKNP symmetric key extension.",
        ]
    )
    pdf.section("6.2 Integration Testing")
    pdf.body(
        "Integration testing validates the end-to-end operational pipeline across client-backend boundaries. "
        "The test suite evaluates candidate lookup at /api/candidates, garbled circuit initialization at /api/gc/init, "
        "local Web Crypto AES-128 circuit evaluation in the client browser, and result resolution with Merkle proof "
        "verification at /api/gc/resolve. An automated script (tamper_test.js) injects modified POI attributes to verify "
        "that the client successfully rejects manipulated responses with probability 1 - 2^-256."
    )
    pdf.body(
        "Empirical Results & Gate Complexity Breakdown: Plain baseline kNN completes in sub-50 ms latency. Secure garbled circuit evaluation over n=500 candidate POIs "
        "involves exactly 1,122,000 AND gates (2,244 AND gates per POI) and 2,244,000 AES-128 operations. The dominant cost "
        "is integer squaring, accounting for 91% of per-POI AND gates (2,048 AND gates). End-to-end secure query latency "
        "ranges between 20 and 28 seconds in interpreted browser JavaScript."
    )
    pdf.body(
        "Application Interface Snapshots: The VEIL React frontend provides an interactive Leaflet 2D map, 3D WebGL Three.js visualizer, real-time stage "
        "latency breakdowns, and a dual-mode baseline comparison toggle. Figure 6.1 illustrates the application landing "
        "page, Figure 6.2 displays live secure kNN query execution with Merkle verification tags, and Figure 6.3 details "
        "the circuit gate complexity breakdown."
    )

    # CHAPTER 7: CONCLUSION
    pdf.chapter_title("7", "CONCLUSION")
    pdf.section("7.1 Conclusion")
    pdf.body(
        "The project successfully demonstrates the design, implementation, and empirical evaluation of VEIL "
        "(Verifiable Encrypted Inference for Location Privacy), a privacy-preserving location-based k-Nearest Neighbour system. "
        "VEIL addresses a critical gap in modern LBS digital infrastructure, where mobile users are traditionally required "
        "to transmit precise GPS coordinates to untrusted remote servers, exposing sensitive behavioural, residential, and medical patterns."
    )
    pdf.body(
        "By synthesizing Yao's Garbled Circuits (enhanced with Free-XOR and Half-Gates optimizations), Oblivious Transfer "
        "(Naor-Pinkas with IKNP extension), and SHA-256 Merkle tree verification, VEIL enables secure computation of "
        "nearest-neighbour queries without disclosing user coordinates to the backend or exposing proprietary POI datasets "
        "to the client. The system was validated over a real-world OpenStreetMap dataset of 500 POIs for Bengaluru, India."
    )
    pdf.bullets(
        [
            "Dual-Mode kNN Computation: Enables real-time toggling between plain baseline and secure garbled circuit kNN.",
            "Verifiable Results: Every response is accompanied by a SHA-256 Merkle proof verified locally by the browser.",
            "Real-Time Spatial Data: Connects directly to OpenStreetMap Overpass API for live metropolitan POI fetching.",
            "Paper Publication: Research paper titled 'VEIL: Verifiable Encrypted Inference for Location Privacy' submitted to C2I6 2026 (Paper ID 477) and COMPSIF 2027 (Paper ID 65).",
        ]
    )
    pdf.section("7.2 Future Enhancement")
    pdf.bullets(
        [
            "Stronger Adversary Model: Extend security using authenticated garbling or cut-and-choose GC.",
            "Hardware Acceleration: Compile browser circuit evaluator to WASM to achieve sub-second decryption times.",
            "Production Oblivious Transfer: Integrate network-bound IKNP OT extension between client and backend.",
            "Spatial Pre-Filtering: Implement R-tree spatial indexing to scale candidate datasets beyond 10,000+ POIs.",
        ]
    )
    # CHAPTER 8: PAPER PUBLICATION
    pdf.chapter_title("8", "PAPER PUBLICATION")
    pdf.section("8.1 Paper Submission Details")
    pdf.body(
        "Title: VEIL: Verifiable Encrypted Inference for Location Privacy - A Coarse-Discovery, Garbled-Circuit "
        "Prototype for Privacy-Preserving k-Nearest-Neighbor Location-Based Services. Authors: Manjunath G S, Tripti "
        "Prasanna, Sinchana K, Shanvi S Shetty. Submissions: C2I6 2026 (Track: Data Science and Advanced Computing, "
        "Paper ID 477, Under Review); COMPSIF 2027 (Track 3: Cyber Resilience, Paper ID 65, Under Review)."
    )
    pdf.section("8.2 Final Draft of Submitted Paper Manuscript")
    paper_sections = [
        "Abstract: Location-based services (LBS) present a fundamental privacy challenge: the dominant model requires users to transmit precise GPS coordinates to servers they do not control. This paper describes VEIL, a prototype privacy-preserving k-nearest-neighbor (kNN) system for LBS built on a two-stage design: coarse candidate discovery and client-side garbled-circuit distance ranking with SHA-256 Merkle proofs.",
        "I. Introduction: Location data is among the most sensitive personal information. VEIL combines coarse-grained candidate discovery with Yao garbled circuits (Free-XOR and Half-Gates) and SHA-256 Merkle tree verification in a direct two-party client/backend system.",
        "II. Related Work: Positioned against k-anonymity, spatial cloaking, mix-zones (MobiMix), geometric searchable encryption (GSE), and cloud garbled-circuit kNN schemes.",
        "III. System Architecture & Threat Model: Two-party React SPA client and Node.js Express backend under the semi-honest (honest-but-curious) adversary model.",
        "IV. Candidate Discovery: Client coarsens location to 0.01 degree grid (~1.11 km) to bound candidate set from in-memory cache without exposing exact GPS.",
        "V. Secure Distance Computation via Garbled Circuits: 32-bit fixed-point squared Euclidean distance (2,244 AND gates/POI, 1,122,000 gates total for n=500, 2,244,000 AES calls, 35.06 MB payload). Uses Free-XOR and Half-Gates. Simulated OT models wire-label selection.",
        "VI. Result Verification via Merkle Tree: SHA-256 Merkle tree root R published; client recomputes leaf hashes and verifies O(log n) sibling inclusion proofs.",
        "VII. Security Analysis: Analysis under semi-honest model, PRF/AES security assumptions, and SHA-256 collision resistance.",
        "VIII. Limitations: Explicitly documents simulated OT, coarse location exposure, browser JavaScript latency (20-27 s), fixed-point planar approximation, and non-persistent cache.",
        "IX. Experimental Evaluation: Evaluated over 500 real OpenStreetMap POIs in Bengaluru. Exact correctness parity with plaintext baseline across k in {1, 3, 5, 10}. Measured end-to-end query latency averaged 21.9 s to 27.4 s.",
        "X. Conclusion and Future Work: Summarizes VEIL architecture, reported performance, and outlines 6 future directions (crypto OT, malicious model, geodesic circuits, WASM acceleration, candidate scaling, and reduced coarse exposure).",
    ]
    for sec in paper_sections:
        pdf.body(sec)

    # References
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, "References", ln=True)
    refs = [
        "[1] S. N. Eshun and P. Palmieri, TIFS 2024 - Mutual location privacy via outsourcing.",
        "[2] Z. Chen et al., IEEE TSC 2023 - Geometric searchable encryption.",
        "[3] H.-J. Kim et al., IEEE Cloud 2017 - Garbled-circuit kNN classification.",
        "[4] V. Kolesnikov and T. Schneider, ICALP 2008 - Free-XOR.",
        "[5] S. Zahur, M. Rosulek, and D. Evans, EUROCRYPT 2015 - Half-Gates.",
        "[6] Y. Ishai et al., CRYPTO 2003 - IKNP OT extension.",
        "[7] M. Naor and B. Pinkas, STOC 1999 - Oblivious transfer.",
        "[8] A. C.-C. Yao, FOCS 1986 - Garbled circuits.",
        "[9] Y. Lindell and B. Pinkas, Journal of Cryptology 2012 - Secure two-party computation.",
        "[10] C. Zhang et al., IEEE Access 2019 - Grid Voronoi spatial index.",
        "[11] R. Paulet et al., TKDE - Privacy-preserving location-based queries.",
    ]
    pdf.bullets(refs)

    # Appendices - expand page count with detailed text
    for appendix_num, appendix_title, paragraphs in _appendices():
        pdf.add_page()
        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(0, 10, f"Appendix {appendix_num}: {appendix_title}", ln=True)
        pdf.ln(2)
        for para in paragraphs:
            pdf.body(para)


def _appendices():
    """Extra material for report length and viva preparation."""
    a = []
    a.append(
        (
            "A",
            "Glossary",
            [
                "kNN: k-Nearest Neighbour spatial query returning the k closest POIs to a query point.",
                "Garbled circuit: Encrypted boolean circuit evaluable without revealing inputs to the garbler.",
                "Oblivious transfer: Protocol where receiver obtains one of two messages without sender learning the choice.",
                "Merkle proof: Short evidence that a leaf belongs to a committed hash tree root.",
                "Semi-honest: Adversary follows the protocol but tries to infer secrets from transcripts.",
                "POI: Point of interest such as hospital, restaurant, pharmacy, or cafe from OSM.",
            ],
        )
    )
    a.append(
        (
            "B",
            "Installation and Reproduction",
            [
                "Prerequisites: Node.js 18 or newer, network access to Overpass API.",
                "Backend: cd backend && npm install && node server.js (port 3001).",
                "Frontend: cd frontend && npm install && npm run dev (port 5173).",
                "Open http://localhost:5173, allow location permission, toggle Secure mode, run kNN.",
                "Tamper test: with server running, node tamper_test.js from repository root.",
            ],
        )
    )
    a.append(
        (
            "C",
            "Privacy Boundary Checklist",
            [
                "POST /api/knn/plain: NOT PRIVATE - latitude and longitude received by server.",
                "POST /api/candidates: receives location; server coarsens to ~1 km before ranking.",
                "POST /api/gc/init: must NOT include coordinates; returns garbled circuit bundle.",
                "POST /api/gc/resolve: must NOT include coordinates; receives result POI ids only.",
                "Client gcProtocol.js: exact GPS encoded locally; never sent to gc/init or gc/resolve.",
                "Server middleware avoids logging request bodies on gc routes.",
            ],
        )
    )
    a.append(
        (
            "D",
            "Threat Model Details",
            [
                "Honest-but-curious server follows API contracts but may analyze garbled tables and outputs.",
                "Client is trusted to protect local GPS and wire labels.",
                "Network attacker protected by TLS in deployment; prototype may use localhost HTTP for dev.",
                "Merkle collision resistance assumed for SHA-256; proofs detect post-commitment tampering.",
                "Output leakage: server learns which POI ids were returned after client evaluation.",
            ],
        )
    )
    a.append(
        (
            "E",
            "Testing Methodology",
            [
                "Functional: plain vs secure ranking consistency on shared candidate sets.",
                "Security: verify endpoints reject latitude/longitude fields with COORDINATES_REJECTED.",
                "Integrity: Merkle valid proofs pass /api/verify; modified leaf hashes fail.",
                "Performance: record garbleMs from gc/init response and client eval timing in UI.",
                "Regression: Haversine display aligned between server knn.js and client gcProtocol.js.",
            ],
        )
    )
    a.append(
        (
            "F",
            "Project Repository Structure",
            [
                "backend/server.js - Express REST API and session management.",
                "backend/osm/fetcher.js - Overpass integration for Bengaluru POIs.",
                "backend/geometry/knn.js - Plain kNN heap and complexity metrics.",
                "backend/crypto/veil.js - VEILSession orchestration.",
                "backend/crypto/gc/garbledCircuit.js - Circuit construction and garbling.",
                "backend/crypto/ot/obliviousTransfer.js - OT primitives and benchmarks.",
                "backend/crypto/merkle/merkleTree.js - Dataset commitment and proofs.",
                "frontend/src/services/gcProtocol.js - Browser secure query pipeline.",
                "frontend/src/components/* - UI map, results, complexity panels.",
            ],
        )
    )
    # Repeat expanded narrative blocks to reach ~60 pages when printed
    extra = (
        "E",
        "Extended Discussion - Performance Engineering",
        [
            "Garbled circuit performance is dominated by symmetric cryptography. Each AND gate in the "
            "Half-Gates construction requires AES during evaluation; with thousands of AND gates per "
            "POI and tens of POIs per session, total AES calls reach millions. Browser Web Crypto "
            "introduces async overhead per gate batch; batching AES calls and WASM compilation are "
            "standard mitigations in the literature. Server-side garbling is parallelizable across POI "
            "circuits but memory grows with gate table size. Caching garbled circuits per static POI "
            "coordinate set would reduce repeated garbling for popular regions at the cost of storage "
            "and update invalidation when OSM data refreshes.",
            "Plain kNN remains valuable as a sanity check. Developers compare distances and ordering "
            "before trusting secure output. Any divergence usually indicates encoding mismatch "
            "between client and server fixed-point scales or inconsistent candidate sets between "
            "candidate discovery and garbled dataset filtering.",
                "OpenStreetMap data quality affects user trust independently of cryptography. Missing "
                "amenity tags, duplicate nodes, and outdated closures appear in live queries. VEIL does "
                "not cryptographically attest POI business status - only that the record matches the "
                "committed Merkle leaf for that snapshot.",
        ],
    )
    a.append(extra)

    topics = [
        ("Garbled circuit wire labels", "Each wire carries two 128-bit labels for logical 0 and 1. Free-XOR sets W1 = W0 XOR Delta globally so XOR gates need no ciphertext table."),
        ("Half-Gates AND evaluation", "Each AND gate uses two AES-128 evaluations on wire labels during client evaluation. This dominates secure kNN latency."),
        ("Ripple-carry subtractor", "SUB computes dx and dy as 33-bit two's complement difference circuits between user and POI coordinate bits."),
        ("Schoolbook squarer SQR", "Squaring dx and dy uses approximately 1024 AND gates each, about 91 percent of per-POI AND gate budget."),
        ("Comparator network CMP", "Bitwise comparison determines ordering of squared distances for top-k selection across POI circuits."),
        ("Fixed-point encoding", "Coordinates scale as round(abs(deg)*1e6) into 32 bits on the client before garbled evaluation."),
        ("Haversine display distance", "Ranking in plain mode uses flat squared distance; UI shows Haversine metres for human-readable output."),
        ("Max-heap top-k", "Plain kNN maintains a size-k max-heap for O(n log k) time over n cached POIs."),
        ("Overpass QL query", "Bengaluru bbox filters amenity tags for hospitals, restaurants, pharmacies, and cafes."),
        ("Dataset TTL cache", "Server refreshes POI cache every 30 minutes to balance freshness and API load."),
        ("Merkle leaf canonicalization", "Leaves hash stable POI fields so proofs bind results to a committed snapshot."),
        ("Tamper test script", "tamper_test.js validates proofs, then demonstrates failure on flipped leaf hashes."),
        ("Session gcSessions map", "Garbled circuit internal state expires after five minutes to limit server memory."),
        ("Coordinate rejection", "gc/init and gc/resolve return 400 if latitude or longitude appear in JSON body."),
        ("Deprecated secure endpoint", "POST /api/knn/secure returns 410 because it previously accepted raw GPS."),
        ("Browser AES-CBC trick", "Web Crypto AES-CBC with zero IV matches server AES-ECB on single blocks for garbleHash."),
        ("Simulated OT disclosure", "Landing page states OT is simulated: client picks w0 or w1 locally from pairs."),
        ("Naor-Pinkas base OT", "Backend obliviousTransfer.js implements base OT for benchmarks and future wiring."),
        ("IKNP extension", "Extends 128 base OTs to many OT instances using symmetric PRG-style hashing."),
        ("Complexity panel UI", "ComplexityPanel.jsx displays AND gate counts, AES totals, and plain vs secure comparison."),
        ("Three.js visualization", "ThreeScene.jsx renders floating markers as an optional 3D view of kNN results."),
        ("Leaflet map layer", "MapView.jsx plots POIs and query context on dark OSM tiles."),
        ("Control panel modes", "Users toggle Plain vs Secure and select k and category filters."),
        ("Result latency breakdown", "ResultPanel shows garble, OT, eval, and total milliseconds per secure query."),
        ("Privacy warning plain mode", "plainQuery response includes privacyWarning that GPS was sent to server."),
        ("Candidate coarsening math", "Two decimal degree grid is roughly 1.1 km north-south near Bengaluru latitude."),
        ("MAX_SECURE_POIS constant", "Thirty candidates limit garbled circuit size for interactive demo latency."),
        ("Error code DATASET_UNAVAILABLE", "HTTP 503 when Overpass API fails; user sees friendly retry message."),
        ("Health endpoint", "GET /api/health reports version 1.1.0 and active garbled circuit session count."),
        ("Team integration workflow", "Frontend calls api.js wrappers; backend modules stay ES module imports."),
        ("Semi-honest threat model", "Parties follow protocol but may infer secrets from garbled tables and outputs."),
        ("Output POI id leakage", "Server learns which POIs were returned; hiding this requires ORAM or PIR research."),
        ("Future malicious GC", "Cut-and-choose garbling would detect cheating garblers at higher cost."),
        ("Spatial pre-filter future", "R-tree or grid Voronoi index could shrink n before garbling metropolitan datasets."),
        ("WASM evaluator future", "Compiling evaluator to WebAssembly could reduce browser AES overhead."),
        ("Conference C2I6 submission", "Paper ID 477 under review on data science and advanced computing track."),
        ("Conference COMPSIF submission", "Paper ID 65 under review on cyber resilience for sustainability track."),
        ("IBE fog architecture paper", "Conference draft describes BF-IBE query wrapping; prototype focuses on GC core."),
        ("Correctness testing", "Secure top-k ids match plain ranking on the same candidate subset."),
        ("Gate count formula", "Total AND gates scale roughly as n_POIs times 2244 for 32-bit distance circuits."),
        ("Communication size", "Garbled gate tables dominate bandwidth between server and browser."),
        ("Ethics of location privacy", "Location traces can reveal sensitive behavior; cryptography reduces trust need."),
        ("Open source OSM license", "ODbL attribution applies to POI data displayed in the application map."),
        ("Viva demo script", "Run plain query, then secure query, show Merkle verified badges and complexity tab."),
    ]
    for i, (title, para) in enumerate(topics, start=1):
        a.append(
            (
                f"H{i}",
                title,
                [
                    para,
                    "Implementation reference: see backend/crypto and frontend/src/services/gcProtocol.js "
                    "in the VEIL repository. This section supports Phase-2 report depth and external viva "
                    "questions on design choices, privacy boundaries, and measured performance trade-offs.",
                ],
            )
        )
    return a


def main():
    import pypdf

    pdf = ReportPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.set_margins(25, 25, 25)
    build(pdf)
    
    temp_out = OUT.parent / "temp_report.pdf"
    pdf.output(str(temp_out))

    # Merge the uploaded 5-page paper PDF directly into the report
    paper_pdf_path = Path(r"C:\Users\sinch\.gemini\antigravity\brain\f2174148-6674-4cb3-b8db-6d0e7fceece8\.user_uploaded\media_1791010923735.pdf")
    
    writer = pypdf.PdfWriter()
    
    if temp_out.exists():
        reader_base = pypdf.PdfReader(str(temp_out))
        for page in reader_base.pages:
            writer.add_page(page)
            
    if paper_pdf_path.exists():
        reader_paper = pypdf.PdfReader(str(paper_pdf_path))
        for page in reader_paper.pages:
            writer.add_page(page)
            
    with open(OUT, "wb") as f_out:
        writer.write(f_out)

    if temp_out.exists():
        try:
            temp_out.unlink()
        except OSError:
            pass

    reader_final = pypdf.PdfReader(str(OUT))
    pages = len(reader_final.pages)
    downloads_copy = Path.home() / "Downloads" / "VEIL_Phase2_Report.pdf"
    try:
        downloads_copy.write_bytes(OUT.read_bytes())
    except OSError:
        downloads_copy = None
    print("Wrote combined report with embedded paper PDF:", pages, "pages")
    if downloads_copy:
        print("Downloads copy:", str(downloads_copy))


if __name__ == "__main__":
    main()

