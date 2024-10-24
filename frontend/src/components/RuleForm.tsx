import React, { useState } from 'react';
import { api } from '../services/api';
import { RuleCreate } from '../types';

export const RuleForm: React.FC = () => {
    const [name, setName] = useState('');
    const [ruleString, setRuleString] = useState('');
    
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const rule: RuleCreate = { name, rule_string: ruleString };
            await api.createRule(rule);
            setName('');
            setRuleString('');
            alert('Rule created successfully!');
        } catch (error) {
            alert('Error creating rule: ' + error.message);
        }
    };
    
    return (
        <form onSubmit={handleSubmit} className="space-y-4">
            <div>
                <label className="block">Rule Name:</label>
                <input
                    type="text"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    className="border p-2 w-full"
                    required
                />
            </div>
            <div>
                <label className="block">Rule String:</label>
                <textarea
                    value={ruleString}
                    onChange={(e) => setRuleString(e.target.value)}
                    className="border p-2 w-full h-32"
                    required
                />
            </div>
            <button
                type="submit"
                className="bg-blue-500 text-white px-4 py-2 rounded"
            >
                Create Rule
            </button>
        </form>
    );
};