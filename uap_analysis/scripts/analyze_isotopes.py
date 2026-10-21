
import json

def calculate_anomaly_score(uap_sample, earth_standard):
    '''Calculate isotopic anomaly score for a UAP sample.'''
    score = 0
    for isotope, uap_ratio in uap_sample.items():
        earth_ratio = earth_standard.get(isotope, 0)
        score += abs(uap_ratio - earth_ratio)
    return score

def analyze_isotopes(json_path):
    '''Analyze isotopic anomalies in UAP materials.'''
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    # Example Earth standards (simplified)
    earth_standards = {
        "Bi-209": 100.0,
        "Mg-26": 11.0,
        "Al-27": 100.0,
        "Cu-63": 69.17
    }
    
    for sample in data['samples']:
        sample_id = sample['sample_id']
        uap_isotopes = sample['elements']
        anomaly_score = calculate_anomaly_score(uap_isotopes, earth_standards)
        print(f"Sample {sample_id}: Anomaly Score = {anomaly_score:.2f}")

if __name__ == "__main__":
    analyze_isotopes("data/raw/uap_materials.json")
