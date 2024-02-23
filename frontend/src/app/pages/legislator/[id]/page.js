'use client'

import LegislatorDetail from '../../../../components/LegislatorDetail';

function LegislatorDetailPage({params}) {


  return (
    <div>
      {params.id && <LegislatorDetail legislatorId={params.id} />}
    </div>
  );
}

export default LegislatorDetailPage;
