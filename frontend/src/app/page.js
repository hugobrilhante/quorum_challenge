"use client"
import LegislatorList from "@/components/LegislatorList";
import BillsList from "@/components/BillList";
import Header from "@/components/Header";

export default function Home() {
    return (
        <div className="flex font-light ">
            <LegislatorList/>
            <BillsList/>
        </div>
    );
}
