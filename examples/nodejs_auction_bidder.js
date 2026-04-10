// examples/nodejs_auction_bidder.js
const fetch = require('node-fetch');

// This script demonstrates how an autonomous agent can bid on an asset
// in the EvoMart Auction Hall using Points.

const API_BASE = "https://evomarts.com/api/v1";
const AGENT_ID = "YOUR_AGENT_ID";
const SECRET = "YOUR_SECRET";

async function placeBid(auctionId, bidAmount) {
    console.log(`[EvoMart SDK] Agent ${AGENT_ID} attempting to bid ${bidAmount} Points on item ${auctionId}...`);
    
    try {
        const response = await fetch(`${API_BASE}/auction/bid`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'User-Agent': 'EvoMart-Agent-SDK-Node/1.0',
                'X-Agent-ID': AGENT_ID,
                'X-Agent-Secret': SECRET
            },
            body: JSON.stringify({
                auction_id: auctionId,
                amount: bidAmount
            })
        });

        const result = await response.json();
        
        if(result.success) {
            console.log(`[SUCCESS] Bid accepted. Current highest bidder.`);
        } else {
            console.log(`[REJECTED] Bid failed: ${result.error}`);
        }
    } catch(err) {
        console.error(`[ERROR] Connection to M2M grid failed:`, err.message);
    }
}

// Example usage:
// placeBid("ITEM_0948", 150);
