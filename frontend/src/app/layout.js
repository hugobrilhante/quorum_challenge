import {Inter} from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";

const inter = Inter({subsets: ["latin"]});

export const metadata = {
    title: "Quorum",
    description: "Quorum Front",
};

export default function RootLayout({children}) {
    return (
        <html lang="en">
        <body className={inter.className}>
        <main className="flex flex-col items-center justify-between">
            <Header/>
            <p className="text-gray-500">Click on the links below to see details</p>
            {children}
        </main>
        </body>
        </html>
    );
}
