async function query(data) {
    var response = await fetch("https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5",
        {
            headers: { Authorization: "Bearer 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", "Content-type": "application/json" },
            method: "POST",
            body: JSON.stringify(data),
        }
    );
    var result = await response.json();
    return result;
}

var input = { "inputs": "What is Kriya Yoga?" };

query(input).then((response) => {
    console.log(JSON.stringify(response));
});