"""Example usage for Damerau-Levenshtein Skill."""
from client import DamerauLevenshtein

def main():
    print("Executing Damerau-Levenshtein Distance...")
    dist1 = DamerauLevenshtein.distance("antigravity", "antigravtiy")
    print(f"Distance between 'antigravity' and 'antigravtiy': {dist1}")
    assert dist1 == 1, "Single transposition should yield distance 1"

    dist2 = DamerauLevenshtein.distance("kitten", "sitting")
    print(f"Distance between 'kitten' and 'sitting': {dist2}")
    assert dist2 == 3
    print("Damerau-Levenshtein verified successfully!")

if __name__ == "__main__":
    main()
