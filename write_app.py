content = '''import { useState } from "react";

const API = "http://127.0.0.1:8000";

export default function App() {
  const [file, setFile] = useState(null);
  const [sigFile, setSigFile] = useState(null);
  const [sigPreview, setSigPreview] = useState(null);
  const [name, setName] = useState("");
  const [designation, setDesignation] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSigChange = (e) => {
    const f = e.target.files[0];
    if (f) { setSigFile(f); setSigPreview(URL.createObjectURL(f)); }
  };

  const handleUpload = async () => {
    if (!file) return alert("Pehle invoice file select karo!");
    if (!sigFile) return alert("Signature image upload karo!");
    setLoading(true); setError(null); setResult(null);
    const form = new FormData();
    form.append("file", file);
    form.append("signature", sigFile);
    form.append("signatory_name", name);
    form.append("designation", designation);
    try {
      const res = await fetch(`${API}/process`, { method: "POST", body: form });
      const data = await res.json();
      setResult(data);
    } catch (err) { setError("Server se connect nahi ho paya!"); }
    finally { setLoading(false); }
  };

  return (
    <div style={{ fontFamily: "Inter, sans-serif", minHeight: "100vh", background: "#F0F4F9" }}>
      <div style={{ background: "#1E3A5F", padding: "16px 32px" }}>
        <h1 style={{ color: "white", margin: 0, fontSize: 20 }}>InvoiceSign MFD</h1>
        <span style={{ color: "#93BBDE", fontSize: 13 }}>Auto-sign GST Invoices</span>
      </div>
      <div style={{ maxWidth: 700, margin: "40px auto", padding: "0 24px" }}>
        <div style={{ background: "white", borderRadius: 12, padding: 28, boxShadow: "0 1px 4px rgba(0,0,0,.08)", marginBottom: 20 }}>
          <h2 style={{ marginTop: 0, color: "#1E3A5F", fontSize: 16 }}>Signatory Details</h2>
          <div style={{ marginBottom: 16 }}>
            <label style={{ display: "block", fontSize: 13, fontWeight: 600, marginBottom: 6 }}>Name of Signatory</label>
            <input type="text" value={name} onChange={(e) => setName(e.target.value)} style={{ width: "100%", padding: "10px 12px", borderRadius: 8, border: "1.5px solid #D0DAE8", fontSize: 14, boxSizing: "border-box" }} />
          </div>
          <div style={{ marginBottom: 16 }}>
            <label style={{ display: "block", fontSize: 13, fontWeight: 600, marginBottom: 6 }}>Designation</label>
            <input type="text" value={designation} onChange={(e) => setDesignation(e.target.value)} style={{ width: "100%", padding: "10px 12px", borderRadius: 8, border: "1.5px solid #D0DAE8", fontSize: 14, boxSizing: "border-box" }} />
          </div>
          <div>
            <label style={{ display: "block", fontSize: 13, fontWeight: 600, marginBottom: 6 }}>Signature Image</label>
            <input type="file" accept=".jpg,.jpeg,.png" onChange={handleSigChange} style={{ display: "block", marginBottom: 10, fontSize: 13 }} />
            {sigPreview && <img src={sigPreview} alt="sig" style={{ maxHeight: 60, border: "1px dashed #ccc", padding: 8, borderRadius: 8 }} />}
          </div>
        </div>
        <div style={{ background: "white", borderRadius: 12, padding: 28, boxShadow: "0 1px 4px rgba(0,0,0,.08)" }}>
          <h2 style={{ marginTop: 0, color: "#1E3A5F", fontSize: 16 }}>Upload GST Invoice</h2>
          <input type="file" accept=".pdf,.zip" onChange={(e) => setFile(e.target.files[0])} style={{ display: "block", marginBottom: 20, fontSize: 13 }} />
          <button onClick={handleUpload} disabled={loading} style={{ background: loading ? "#93BBDE" : "#1E3A5F", color: "white", border: "none", padding: "12px 28px", borderRadius: 8, fontSize: 15, fontWeight: 600, cursor: "pointer", width: "100%" }}>
            {loading ? "Processing..." : "Sign Invoices"}
          </button>
        </div>
        {error && <div style={{ background: "#FEE2E2", color: "#B91C1C", padding: 16, borderRadius: 8, marginTop: 20 }}>{error}</div>}
        {result && (
          <div style={{ background: "white", borderRadius: 12, padding: 28, marginTop: 20, boxShadow: "0 1px 4px rgba(0,0,0,.08)" }}>
            <h2 style={{ marginTop: 0, color: "#16A34A" }}>{result.processed} Invoice(s) Signed!</h2>
            <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13, marginBottom: 20 }}>
              <thead><tr style={{ background: "#EEF2F7" }}>
                <th style={{ padding: "8px 12px", textAlign: "left" }}>Filename</th>
                <th style={{ padding: "8px 12px", textAlign: "left" }}>Invoice No.</th>
                <th style={{ padding: "8px 12px", textAlign: "left" }}>Date</th>
                <th style={{ padding: "8px 12px", textAlign: "left" }}>Status</th>
              </tr></thead>
              <tbody>{result.results.map((r, i) => (
                <tr key={i} style={{ borderBottom: "1px solid #F0F4F9" }}>
                  <td style={{ padding: "8px 12px" }}>{r.filename}</td>
                  <td style={{ padding: "8px 12px" }}>{r.invoice_no}</td>
                  <td style={{ padding: "8px 12px" }}>{r.invoice_date}</td>
                  <td style={{ padding: "8px 12px", color: "#16A34A", fontWeight: 600 }}>{r.status}</td>
                </tr>
              ))}</tbody>
            </table>
            <a href={`${API}${result.download_url}`} style={{ background: "#16A34A", color: "white", padding: "12px 28px", borderRadius: 8, textDecoration: "none", fontWeight: 600, fontSize: 15, display: "inline-block" }}>
              Download Signed Files + Excel Report
            </a>
          </div>
        )}
      </div>
    </div>
  );
}'''

with open(r'C:\Users\user\OneDrive\Desktop\invoicesign-frontend\src\App.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("App.jsx successfully written!")python write_app.py