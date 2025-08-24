const mappings = {
    // Simple vowel mappings
    'a': 'า',
    'e': 'เ',
    'i': 'ิ',
    'o': 'โ',
    'u': 'ุ',
    'ă': 'แ',  // example
    'â': 'เ',  // example
    // Add more mappings as needed
};

// Function to apply mappings
function transcribe() {
    let inputText = document.getElementById("input").value;
    let outputText = inputText;

    // Sort keys by length to handle digraphs first
    const keys = Object.keys(mappings).sort((a, b) => b.length - a.length);

    keys.forEach(key => {
        let regex = new RegExp(key, 'g');
        outputText = outputText.replace(regex, mappings[key]);
    });

    document.getElementById("output").value = outputText;
}
