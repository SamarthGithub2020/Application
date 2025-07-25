from dataclasses import dataclass # acts as a decorator which creates a variable for a empty class

@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str