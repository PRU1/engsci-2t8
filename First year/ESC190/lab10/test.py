import csv
from io import StringIO

csv_data = """Date,Character,Age,HeightCm,AppleCount,MoodRating
2025-01-15,Snow White,14,157.5,1,8.5
Doc,200,91.4,3,7.2
2025-01-16,Grumpy,199,89.0,0,3.4
2025-01-16,202,94.0,2,9.7
2025-01-17,Sleepy,202,90.2,1,6.3
Bashful,198,88.5,1,5.8
2025-01-18,Sneezy,197,92.3,2,7.4
2025-01-18,Dopey,195,87.1,4,8.9
2025-01-19,,42,175.6,0,2.1
Prince,25,185.3,2,9.5
2025-01-20,Huntsman,38,178.4,1,6.7
2025-01-20,250,92.0,3,7.3
3
2025-01-21,Forest Animals,5,30.5,4,9.2
"""

def parse_csv(csv_content):
    f = StringIO(csv_content)
    reader = csv.reader(f)
    headers = next(reader)
    
    result = {}
    current_date = None
    
    for row in reader:
        if len(row) < 6:
            # Skip incomplete rows
            continue

        if row[0]:
            # Date is present in the row
            current_date = row[0]
        
        if not current_date:
            # If there's still no date, skip this entry
            continue
        
        # Handle rows where the date might not be included
        character = row[1] if row[0] else row[0]
        data = row[1:] if row[0] else row[0:]

        # Prepare entry
        entry = {
            "Character": data[0],
            "Age": int(data[1]),
            "HeightCm": float(data[2]),
            "AppleCount": int(data[3]),
            "MoodRating": float(data[4])
        }
        
        # Add entry under current date
        if current_date not in result:
            result[current_date] = {}
        
        result[current_date][entry["Character"]] = entry

    return result

parsed_data = parse_csv(csv_data)
print(parsed_data)
