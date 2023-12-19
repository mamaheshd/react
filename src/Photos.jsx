import React,{useEffect} from 'react'
import { useSelector,useDispatch } from 'react-redux'
import { fetchPhotos } from './actions/photoAction'

const Photos = () => {
    const dispatch=useDispatch()
    const photosData= useSelector(store=>store.photosData)
    const photos=photosData.photos
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

export default Photos