import { FETCH_PHOTO_REQUEST,FETCH_PHOTO_SUCCESS,FETCH_PHOTO_FAILURE } from "../constants/photoConstant";
import axios from "axios";
import { API_URLS } from "../apiServer";

export const fetchPhotos=()=>async(dispatch)=>{
    try{
        dispatch({type:FETCH_PHOTO_REQUEST})
        const {data} = await axios.get(`${API_URLS}`)
        dispatch({
            type:FETCH_PHOTO_SUCCESS,
            payload:data
        })
    }
    catch(error){
        dispatch({
            type:FETCH_PHOTO_FAILURE,
            payload:error.message
        })
    }
}
