import json
import csv
from datetime import datetime
from typing import Dict, Any, List, Optional


class GrantSubmissionParser:
    """Parser for grant submissions"""
    
    def __init__(self):
        self.csv_columns = [
            "Organization Legal Name", "Grant Submission Name", "Stage",
            "Requested Amount", "Awarded Amount", "Grant Type", "Tags",
            "Pipeline/Workflow Associated", "Duration Start", "Duration End", 
            "Grant Submission Id"
        ]
    
    def parse_file(self, input_file: str, output_file: str):
        """Main method to parse JSON and write CSV."""
        # Load data
        with open(input_file, 'r') as f:
            data = json.load(f)
        
        # Process submissions
        submissions = data.get('responses', [])
        
        # Write CSV
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.csv_columns)
            
            for submission in submissions:
                row = self._extract_row_data(submission)
                writer.writerow(row)
        
        print(f"Processed {len(submissions)} submissions")
    
    def _extract_row_data(self, submission: Dict[str, Any]) -> List[str]:
        """Extract data for one submission row."""
        return [
            self._get_org_name(submission),
            submission.get('name', ''),
            submission.get('stage', ''),
            self._get_requested_amount(submission),
            submission.get('awardedAmount', ''),
            submission.get('grantType', ''),
            self._get_tags_string(submission),
            self._get_pipeline_name(submission),
            self._format_date(submission.get('duration', {}).get('start')),
            self._format_date(submission.get('duration', {}).get('end')),
            submission.get('id', '')
        ]
    
    def _get_org_name(self, submission: Dict[str, Any]) -> str:
        """Get organization name with fallback."""
        return submission.get('nonprofit', {}).get('legalName', '')
    
    def _get_requested_amount(self, submission: Dict[str, Any]) -> str:
        """Get requested amount (min amount from grant_amount)."""
        amount = submission.get('grantAmount', {}).get('minAmount')
        return str(amount) if amount else ''
    
    def _get_tags_string(self, submission: Dict[str, Any]) -> str:
        """Convert tags array to comma-separated string."""
        tags = submission.get('tags', [])
        return ','.join(tags) if tags else ''
    
    def _get_pipeline_name(self, submission: Dict[str, Any]) -> str:
        """Get pipeline name with fallback."""
        pipeline_info = submission.get('pipelineInfo')
        return pipeline_info.get('name', '') if pipeline_info else ''
    
    def _format_date(self, date_str: Optional[str]) -> str:
        """Format ISO date to MM/DD/YY."""
        if not date_str:
            return ''
        try:
            dt = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            return dt.strftime('%m/%d/%y')
        except:
            return ''


def main():
    """Main execution."""
    parser = GrantSubmissionParser()
    parser.parse_file('submissions.json', 'submission_output.csv')
    print("CSV file generated successfully!")


if __name__ == "__main__":
    main()
