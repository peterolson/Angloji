import { similarityData } from "./char_data.js";
import { decipheredData, componentFamilies } from "./deciphered.js";

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
            `<li>
            <img src="/full_set/split/${word.padStart(
                4,
                "0"
            )}.png" width=75 height=75 />
            <span class="details">
                <span>${word.padStart(4, "0")}</span>
                <span>
                ${decipheredText || "undeciphered"}
                </span>
                <span>(${count})</span>
            </span>
            </li>`
        );
    }
    html.push("</ol>");
    document.body.innerHTML += html.join("\n");
}

function showDecipheredData() {
    const html = ["<h2>Deciphered Words</h2>"];
    html.push("<ol>");
    for (const [key, value] of Object.entries(decipheredData).sort((a, b) => {
        return a[1].localeCompare(b[1]) || a[0].localeCompare(b[0]);
    })) {
        html.push(
            `<li>
            <img src="/full_set/split/${key.padStart(
                4,
                "0"
            )}.png" width=75 height=75 />
            <span class="details">
            <span class="deciphered">${value}</span>
            <span>${key.padStart(4, "0")}</span>
            </span>
            </li>`
        );
    }
    html.push("</ol>");
    document.body.innerHTML += html.join("\n");
}

function showComponentFamilies() {
    const html = ["<h2>Component Families</h2>"];
    for (const family of componentFamilies) {
        html.push(`<h3>${family.guess}</h3>`);
        html.push("<ol>");
        for (const example of family.examples) {
            const decipheredText = decipheredData[example];
            html.push(
                `<li>
                <img src="/full_set/split/${example
                    .toString()
                    .padStart(4, "0")}.png" width=75 height=75 />
                <span class="details">
                <span class="deciphered">${
                    decipheredText || "undeciphered"
                }</span>
                <span>${example.toString().padStart(4, "0")}</span>
                </span>
                </li>`
            );
        }
        html.push("</ol>");
    }
    document.body.innerHTML += html.join("\n");
}

function displayPost(post) {
    const postData = similarityData.filter((item) => item.post === post);
    const html = [`<h2>${post}</h2>`];

    html.push("<div class='post'>");
    for (const item of postData) {
        const decipheredText = decipheredData[item.fullSetId];
        const families = componentFamilies
            .filter((family) => family.examples.includes(+item.fullSetId))
            .map((family) => family.guess)
            .join("<br>");
        html.push(`<div class='item'>
            <img src="/full_set/split/${item.fullSetId.padStart(
                4,
                "0"
            )}.png" alt="${item.fullSetId}" width=75 height=75 />
            ${
                decipheredText
                    ? `<span class="deciphered">${decipheredText}</span>`
                    : families
                    ? `<span class="families">${families}</span>`
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
showDecipheredData();
showComponentFamilies();
for (const post of postList) {
    displayPost(post);
}
