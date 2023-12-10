import React,{useState} from 'react'
import { useDispatch } from 'react-redux'

const Form = () => {
    const [name,setName]=useState('')
    const dispatch=useDispatch()
    const changeName=()=>(
        dispatch({type:'CHANGE',payload:name})
    )
  return (
    <>
        <label htmlFor="fname">FullName</label>
        <br />
        <input type="text" name="fname" id="fname" onChange={e=>setName(e.target.value)}/>
        <br />
        <button onClick={changeName}>Submit</button>
    </>
  )
}

export default Form