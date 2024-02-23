'use client'

import BillDetail from '../../../../components/BillDetail';

function BillDetailPage({params}) {
    return (
        <div>
            {params.id && <BillDetail billId={params.id}/>}
            <div className="mt-5">
                <a href={`/`} className="text-blue-500 hover:underline">
                    {"< Back"}
                </a>
            </div>
        </div>
    );
}

export default BillDetailPage;
