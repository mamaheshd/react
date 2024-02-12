import axios from 'axios'
import React,{useEffect,useState} from 'react'
import { API } from './config'

const Posts = () => {
    const[posts,setPosts]=useState([])

    useEffect(()=>{
        axios.get(`${API}/posts`)
        .then(res=>setPosts(res.data))
        .catch(err=>console.log(err))
    },[])
  return (
    <>
    {posts.map((item,i)=>(
        <div key={i}>
            <h1>Title:{item.title}</h1>
            <p>Url:{item.url} </p>
        </div>
    ))}
    </>
  )
}

export default Posts