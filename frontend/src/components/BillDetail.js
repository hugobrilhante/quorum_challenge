"use client"
import React, {useState, useEffect} from 'react';
import axios from 'axios';

function BillDetail({billId}) {
    const [bill, setBill] = useState(null);

    useEffect(() => {
        async function fetchBillDetail() {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/bills/${billId}`);
                setBill(response.data);
            } catch (error) {
                console.error('Error fetching bill detail:', error);
            }
        }

        fetchBillDetail();
    }, [billId]);

    if (!bill) {

        return (
            <div className="container mx-auto">
                <p>Loading...</p>
            </div>);
    }

    return (
        <div className="container mx-auto">
            <h1 className="text-2xl font-bold my-4">Bill Detail</h1>
            <table className="table-auto">
                <thead>
                <tr>
                    <th className="border px-4 py-2">ID</th>
                    <th className="border px-4 py-2">Bill</th>
                    <th className="border px-4 py-2">Supporters</th>
                    <th className="border px-4 py-2">Opposers</th>
                    <th className="border px-4 py-2">Primary Sponsor</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td className="border px-4 py-2">{bill.id}</td>
                    <td className="border px-4 py-2">{bill.title}</td>
                    <td className="border px-4 py-2">{bill.supporters}</td>
                    <td className="border px-4 py-2">{bill.opposers}</td>
                    <td className="border px-4 py-2">{bill.sponsor}</td>
                </tr>
                </tbody>
            </table>
        </div>

    );
}

export default BillDetail;
