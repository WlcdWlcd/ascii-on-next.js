import Image from "next/image";
import Ascii from "./components/ascii";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col p-24 bg-slate-600">
        <Ascii/>
    </main>
  );
}
