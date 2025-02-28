from mrjob.job import MRJob
from mrjob.step import MRStep

class HealthDataAnalysis(MRJob):
    
    def mapper(self, _, line):
        parts = line.split(',')
        if parts[0] != "PatientID":  # Skip header
            age = int(parts[1])
            bp = float(parts[2])
            sugar = float(parts[3])
            cholesterol = float(parts[4])
            hb = float(parts[5])
            yield age, (bp, sugar, cholesterol, hb, 1)

    def reducer(self, key, values):
        total_bp = total_sugar = total_cholesterol = total_hb = count = 0
        for bp, sugar, cholesterol, hb, c in values:
            total_bp += bp
            total_sugar += sugar
            total_cholesterol += cholesterol
            total_hb += hb
            count += c
        yield key, (round(total_bp/count, 2), round(total_sugar/count, 2), round(total_cholesterol/count, 2), round(total_hb/count, 2))
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer)
        ]

if __name__ == "__main__":
    HealthDataAnalysis.run()
