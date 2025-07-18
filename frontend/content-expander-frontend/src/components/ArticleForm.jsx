import React, { useEffect, useState } from 'react';
import axios from '../api/axiosInstance';
const OUTPUT_OPTIONS = ["twitter", "youtube", "instagram"]

export default function ArticleForm() {

  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")
  const [outputs, setOutputs] = useState(["twitter"])
  const [results, setResults] = useState({})
  const [loading, setLoading] = useState(false)

  const toggleOutput = (opt) => {
    setOutputs((prev) =>
      prev.includes(opt) ? prev.filter(o => o !== opt) : [...prev, opt]
    )
  }

  const handleSubmit = async () => {
    setLoading(true)
    setResults({})
    const res = await fetch("http://localhost:8080/api/content_expand", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, content, outputs })
    })
    const json = await res.json()
    setResults(json.outputs)
    setLoading(false)
  }

  return (
    <div className="min-h-screen bg-gray-100 p-6 text-gray-800">
      <div className="max-w-3xl mx-auto bg-white rounded-xl shadow-md p-6 space-y-4">
        <h1 className="text-3xl font-bold">Repaste</h1>
        <input
          type="text"
          placeholder="Title"
          className="w-full border px-3 py-2 rounded"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          placeholder="Paste your blog post content here..."
          className="w-full border px-3 py-2 rounded h-48"
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <div className="space-x-3">
          {OUTPUT_OPTIONS.map(opt => (
            <label key={opt} className="inline-flex items-center space-x-1">
              <input
                type="checkbox"
                checked={outputs.includes(opt)}
                onChange={() => toggleOutput(opt)}
              />
              <span className="capitalize">{opt}</span>
            </label>
          ))}
        </div>
        <button
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
          onClick={handleSubmit}
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate Outputs"}
        </button>

        {Object.entries(results).length > 0 && (
          <div className="mt-6 space-y-4">
            {Object.entries(results).map(([key, val]) => (
              <div key={key}>
                <h2 className="text-xl font-semibold capitalize">{key}</h2>
                <pre className="bg-gray-100 p-3 rounded whitespace-pre-wrap">{val}</pre>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )

}