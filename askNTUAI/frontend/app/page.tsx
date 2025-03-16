"use client";
import { useState } from "react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

export default function Home() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askQuestion = async () => {
    if (!question) return;
    setLoading(true);
    setAnswer("");

    try {
      const res = await fetch("http://192.168.0.125:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });

      const data = await res.json();
      setAnswer(data.answer);
    } catch (error) {
      setAnswer("Error fetching response. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <Card className="w-full max-w-lg p-6 shadow-lg rounded-2xl">
        <h1 className="text-2xl font-bold mb-4 text-center">NTU AI Chatbot</h1>
        <Input
          placeholder="Ask a question..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          className="mb-4"
        />
        <Button onClick={askQuestion} disabled={loading} className="w-full">
          {loading ? "Thinking..." : "Ask NTU AI"}
        </Button>
        {answer && (
          <CardContent className="mt-4 p-4 bg-gray-50 rounded-lg shadow">
            <p className="text-gray-700">{answer}</p>
          </CardContent>
        )}
      </Card>
    </div>
  );
}
