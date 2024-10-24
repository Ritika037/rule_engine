import axios from 'axios';
import { Rule, RuleCreate, RuleEvaluation } from '../types';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const api = {
    createRule: async (rule: RuleCreate): Promise<Rule> => {
        const response = await axios.post(`${API_URL}/rules`, rule);
        return response.data;
    },
    
    evaluateRule: async (ruleId: number, data: Record<string, any>): Promise<boolean> => {
        const response = await axios.post(`${API_URL}/rules/${ruleId}/evaluate`, { data });
        return response.data.result;
    },
    
    combineRules: async (ruleIds: number[]): Promise<string> => {
        const response = await axios.post(`${API_URL}/rules/combine`, ruleIds);
        return response.data.combined_rule_string;
    }
};