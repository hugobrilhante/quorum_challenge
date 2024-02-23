"use client"
import React, {useState, useEffect} from 'react';

import axios from 'axios';

function LegislatorList() {
    const [legislators, setLegislators] = useState([]);

    useEffect(() => {
        async function fetchLegislators() {
            try {
                const response = await axios.get('http://127.0.0.1:8000/legislators/');
                setLegislators(response.data);
            } catch (error) {
                console.error('Error fetching legislators:', error);
            }
        }

        fetchLegislators();
    }, []);

    return (
        <div className="container mx-auto">
            <h1 className="text-2xl font-bold my-4">Legislator List</h1>
            <ul>
                {legislators.map(function (legislator) {
                    return (
                        <li key={legislator.id} className="my-2">
                            <a href={`/legislator/${legislator.id}`} className="text-blue-500 hover:underline">
                                {legislator.name}
                            </a>
                        </li>
                    );
                })}
            </ul>
        </div>
    );
}

export default LegislatorList;
