"use client"
import React,{useState} from "react";

import PropertiesForm from "./properties-form";


export default function Ascii (props){

    const [ascii,setAscii] = useState()

    const handleAsciiChange = (ascii) => {
        setAscii(ascii)
    } 


    const element = (<div>
        <PropertiesForm handleAsciiChange={handleAsciiChange} />
        <div className="text-center bg-black">
            <pre className="text-white mt-5 overflow-y-hidden" >{ascii}</pre>
        </div>
        




    </div>)

    return element

}