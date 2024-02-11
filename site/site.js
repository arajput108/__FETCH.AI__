// script.js
document.addEventListener("DOMContentLoaded", function() {
    const searchButton = document.getElementById("search-button");
    const searchResults = document.getElementById("search-results");

    searchButton.addEventListener("click", function() {
        const destination = document.getElementById("destination").value;
        const checkInDate = document.getElementById("check-in-date").value;
        const checkOutDate = document.getElementById("check-out-date").value;

        // Simulate API call to fetch search results
        const results = [
            { name: "Hotel A", price: "$100" },
            { name: "Hotel B", price: "$120" },
            { name: "Hotel C", price: "$150" }
        ];

        // Clear previous results
        searchResults.innerHTML = "";

        // Display results
        results.forEach(function(result) {
            const resultItem = document.createElement("div");
            resultItem.classList.add("result-item");
            resultItem.innerHTML = `
                <h3>${result.name}</h3>
                <p>Price: ${result.price}</p>
            `;
            searchResults.appendChild(resultItem);
        });
    });
});
