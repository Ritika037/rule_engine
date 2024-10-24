import React, { useState } from 'react';
import { api } from '../services/api';

export const RuleEvaluator: React.FC = () => {
    const [ruleId, setRuleId] = useState('');
    const [inputData, setInputData] = useState('');
    const [result, setResult] = useState<boolean | null>(null);
    
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const data = JSON.parse(inputData);
            const evaluationResult = await api.evaluateRule(Number(ruleId), data);
            setResult(evaluationResult);
        } catch (error) {
            alert('Error evaluating rule: ' + error.message);
        }
    };
    
    return (
        <div className="space-y-4">
            <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                    <label className="block">Rule ID:</label>
                    <input
                        type="number"
                        value={ruleId}
                        onChange={(e) => setRuleId(e.target.value)}
                        className="border p-2 w-full"
                        required
                    />
                </div>
                <div>
                    <label className="block">Input Data (JSON):</label>
                    <textarea
                        value={inputData}
                        onChange={(e) => setInputData(e.target.value)}
                        className="border p-2 w-full h-32"
                        required
                    />
                </div>
                <button
                    type="submit"
                    className="bg-green-500 text-white px-4 py-2 rounded"
                >
                    Evaluate Rule
                </button>
            </form>
            
            {result !== null && (
                <div className={`p-4 rounded ${result ? 'bg-green-100' : 'bg-red-100'}`}>
                    Result: {result ? 'True' : 'False'}
                </div>
            )}
        </div>
    );
};