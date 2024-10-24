export interface Rule {
    id: number;
    name: string;
    rule_string: string;
    created_at: string;
    updated_at: string;
}

export interface RuleCreate {
    name: string;
    rule_string: string;
}

export interface RuleEvaluation {
    rule_id: number;
    input_data: Record<string, any>;
    result: boolean;
}