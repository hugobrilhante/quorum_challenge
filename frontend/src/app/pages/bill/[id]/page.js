'use client'

import BillDetail from '../../../../components/BillDetail';

function BillDetailPage({params}) {


  return (
    <div>
      {params.id && <BillDetail billId={params.id} />}
    </div>
  );
}

export default BillDetailPage;
