"use client"
import React, {useState, useEffect} from 'react';
import axios from 'axios';

function BillsList() {
    const [bills, setBills] = useState([]);

    useEffect(() => {
        async function fetchBills() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/bills/');
                setBills(response.data);
            } catch (error) {
                console.error('Error fetching bills:', error);
            }
        }

        fetchBills();
    }, []);

    return (
        <div className="container mx-auto">
            <h1 className="text-2xl font-bold my-4">Bill List</h1>
            <ul>
                {bills.map(bill => (
                    <li key={bill.id} className="my-2">
                        <a href={`/bills/${bill.id}`} className="text-blue-500 hover:underline">
                            {bill.title}
                        </a>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default BillsList;
