"use client"
import LegislatorList from "@/components/LegislatorList";
import BillsList from "@/components/BillList";

export default function Home() {
    return (
        <main className="flex flex-col items-center justify-between">
            <LegislatorList/>
            <BillsList/>
        </main>
    );
}
