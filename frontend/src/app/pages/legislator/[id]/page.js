'use client'

import LegislatorDetail from '../../../../components/LegislatorDetail';

function LegislatorDetailPage({params}) {
    return (
        <div>
            {params.id && <LegislatorDetail legislatorId={params.id}/>}
            <div className="mt-5">
                <a href={`/`} className="text-blue-500 hover:underline">
                    {"< Back"}
                </a>
            </div>
        </div>
    );
}

export default LegislatorDetailPage;
