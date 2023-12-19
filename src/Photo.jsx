import React,{useEffect} from 'react'
import { useSelector,useDispatch } from 'react-redux'
import { fetchPhotos } from './actions/photoAction'

const Photo = () => {
    const dispatch=useDispatch()
    const productsData= useSelector(store=>store.productsData)
    const photos=productsData.photo
    useEffect(()=>{
        try{
            dispatch(fetchPhotos())
        }
        catch(error){
            console.log('Error in ferching data')
        }
    },[dispatch])
  return (
    <>
    
    {photos && photos.map(item=>(
            <h2>{item.title} </h2>
        ))}
    </>
  )
}

export default Photo