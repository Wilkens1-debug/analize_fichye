class CSVStatsAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.strings = []
        self.floats = []
        self.dynamics = []
        self.integers = []
    
    def analyze_csv(self):
        if self.file_exists(self.filename):
            file = open(self.filename, 'r', encoding='latin-1')
            lines = file.readlines()

            column_data = self.get_column_data(lines)
            self.strings = column_data["strings"]
            self.floats = column_data["floats"]
            self.dynamics = column_data["dynamics"]
            self.integers = column_data["integers"]

            file.close()
            return {
                "strings": self.strings,
                "floats": self.floats,
                "dynamics": self.dynamics,
                "integers": self.integers
            }
        else:
            print("Le fichier n'existe pas.")
            return {
                "strings": [],
                "floats": [],
                "dynamics": [],
                "integers": []
            }
    
    def file_exists(self, filename):
        import os
        return os.path.exists(filename)
    
    def get_column_data(self, lines):
        column_data = {
            "strings": [],
            "floats": [],
            "dynamics": [],
            "integers": []
        }
        
        for line in lines:
            values = line.split(',')
            
            for i, value in enumerate(values):
                value = value.strip()
                
                if self.is_integer(value):
                    column_data["integers"].append(int(value))
                elif self.is_float(value):
                    column_data["floats"].append(float(value))
                elif self.is_string(value):
                    column_data["strings"].append(value)
                else:
                    column_data["dynamics"].append(value)
                    
        return column_data
    
    def is_integer(self, value):
        return value.isdigit()
    
    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def is_string(self, value):
        return isinstance(value, str)
    
    def is_dynamic(self, value):
        return not (self.is_integer(value) or self.is_float(value))



