"use client"
import React, {useState, useEffect} from 'react';
import axios from 'axios';

function LegislatorDetail({legislatorId}) {
    const [legislator, setLegislator] = useState(null);

    useEffect(() => {
        async function fetchLegislatorDetail() {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/legislators/${legislatorId}`);
                setLegislator(response.data);
            } catch (error) {
                console.error('Error fetching legislator detail:', error);
            }
        }

        fetchLegislatorDetail();
    }, [legislatorId]);

    if (!legislator) {

        return (
            <div className="container mx-auto">
                <p>Loading...</p>
            </div>);
    }

    return (
        <div className="container mx-auto">
            <h1 className="text-2xl font-bold my-4">Legislator Detail</h1>
            <table className="table-auto">
                <thead>
                <tr>
                    <th className="border px-4 py-2">ID</th>
                    <th className="border px-4 py-2">Name</th>
                    <th className="border px-4 py-2">Supported Bills</th>
                    <th className="border px-4 py-2">Opposed Bills</th>
                </tr>
                </thead>
                <tbody>
                <tr>
                    <td className="border px-4 py-2">{legislator.id}</td>
                    <td className="border px-4 py-2">{legislator.name}</td>
                    <td className="border px-4 py-2">{legislator.supported}</td>
                    <td className="border px-4 py-2">{legislator.opposed}</td>
                </tr>
                </tbody>
            </table>
        </div>

    );
}

export default LegislatorDetail;
