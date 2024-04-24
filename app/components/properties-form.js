'use client'
// import { headers } from 'next/headers';
import React,{useState} from 'react';

import axios from 'axios';


const PropertiesForm = (props) => {
    const [image, setImage] = useState()
    const [ascii, setAscii] = useState()
    const [inverted,setInverted] = useState(true)


    const [sliderSize,setSliderSize] = useState(50)

    const generate = (e) =>{
        if (image !== undefined ){
            e.preventDefault()
            axios.post('http://127.0.0.1:8000/convert', {
                'base64_data': image,
                'sliceSize': sliderSize,
                'invert':inverted
            })
                .then((response) => props.handleAsciiChange(response.data.ascii))

        }

                
    }

    const handleUpload = (e) => {
        
        if (e.target.files[0].size > 3000000) {
            console.log("File too large");
            return;
        }
        let reader = new FileReader();
        reader.readAsDataURL(e.target.files[0]);

        reader.onload = () => {
            setImage(reader.result); //base64encoded string
            generate(e)
        };
        reader.onerror = error => {
            console.log("Error: ", error);
        };
        

    }
    
    
    const element = (<div className="border bg-neutral-700 rounded-2xl p-2 w-1/2  ">
        <form className='flex flex-col ' onSubmit={(e) => generate(e)} >
            <input onChange={(event)=>handleUpload(event)}  type="file" accept = "image/*" className='bg-neutral-500 w-1/2'></input>

                <p>invert symbols <input 
                                type = "checkbox"
                                checked = {inverted}
                                onChange={(event)=>{ 
                                    setInverted(event.target.checked)
                                    generate(event)


                                 }}
                
                ></input></p>

                <p>slice size <input 
                                    type='range'
                                    min='8'
                                    max='100'
                                    step="1"
                                    value = {sliderSize}
                                    onChange={(e) => { 
                                        setSliderSize(parseInt(e.target.value)) 
                                        generate(e)
                                    
                                    }
                                        
                                    
                                    
                                    }
                                    ></input></p>


            {/* {ready && <input type="submit" value="generate" className='w-auto w-1/2'/>} */}
            
        </form>
        <p>{ascii}</p>
        
    </div>) 

    return element
}

export default PropertiesForm;