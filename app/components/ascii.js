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
        <pre className="text-white bg-black mt-5" >{ascii}</pre>




    </div>)

    return element

}