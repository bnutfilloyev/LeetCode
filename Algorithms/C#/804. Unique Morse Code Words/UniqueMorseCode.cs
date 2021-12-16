public class Solution {
    public int UniqueMorseRepresentations(string[] words) {
          string[] morse = { ".-", "-...", "-.-.", "-..", ".", "..-.",
                "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", 
                "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", 
                ".--", "-..-", "-.--", "--.." };

            List<string> Morsed= new List<string>();

            foreach (string word in words)
            {
                string x = "";
                for (int i = 0; i < word.Length; i++)
                {
                    x += morse[word[i] - 97];
                }
                Morsed.Add(x);
            }
            return Morsed.Distinct().ToList().Count();
    }
}