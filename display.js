import { similarityData } from "./char_data.js";
import { decipheredData } from "./deciphered.js";

console.log("Similarity Data:", similarityData);

const posts = new Set(similarityData.map((item) => item.post));
const postList = Array.from(posts).sort((a, b) => {
    const numberPart = (str) => parseInt(str.match(/\d+/)[0], 10);
    const alphaPart = (str) => str.match(/[a-zA-Z]+/)[0];
    const aAlpha = alphaPart(a).toLowerCase();
    const bAlpha = alphaPart(b).toLowerCase();
    if (aAlpha === bAlpha) {
        return numberPart(a) - numberPart(b);
    }
    return aAlpha.localeCompare(bAlpha);
});

function displayMostFrequentWords() {
    const wordCount = {};
    for (const item of similarityData) {
        wordCount[item.fullSetId] = (wordCount[item.fullSetId] || 0) + 1;
    }
    const sortedWords = Object.entries(wordCount)
        .sort((a, b) => {
            if (a[1] === b[1]) {
                return a[0].localeCompare(b[0]);
            }
            return b[1] - a[1];
        })
        .filter((item) => item[1] > 1);
    const html = ["<h2>Most Frequent Words</h2>"];
    html.push("<ol>");
    for (const [word, count] of sortedWords) {
        const decipheredText = decipheredData[word];
        html.push(
            `<li>${word.padStart(4, "0")} - ${
                decipheredText || "undeciphered"
            } (${count})</li>`
        );
    }
    html.push("</ol>");
    document.body.innerHTML += html.join("\n");
}

function displayPost(post) {
    const postData = similarityData.filter((item) => item.post === post);
    const html = [`<h2>${post}</h2>`];

    html.push("<div class='post'>");
    for (const item of postData) {
        const decipheredText = decipheredData[item.fullSetId];
        html.push(`<div class='item'>
            <img src="/full_set/split/${item.fullSetId.padStart(
                4,
                "0"
            )}.png" alt="${item.fullSetId}" width=75 height=75 />
            ${
                decipheredText
                    ? `<span class="deciphered">${decipheredText}</span>`
                    : "<span>&nbsp;</span>"
            }
            <span>${item.fullSetId.padStart(4, "0")}</span>
        </div>`);
    }
    html.push("</div>");
    document.body.innerHTML += html.join("\n");
}

console.log("Unique Posts:", postList);

displayMostFrequentWords();
for (const post of postList) {
    displayPost(post);
}
