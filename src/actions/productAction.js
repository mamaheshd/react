import { FETCH_PRODUCT_REQUEST,FETCH_PRODUCT_SUCCESS,FETCH_PRODUCT_FAILURE } from "../constants/productConstant";
import { fetchProducts } from "../apiServer";


export const fetchProductsRequest=()=>({
    type:FETCH_PRODUCT_REQUEST
})

export const fetchProductsSuccess=(products)=>({
    type:FETCH_PRODUCT_SUCCESS,
    payload:products // sent data to container from redux
})

export const fetchProductsFailure=()=>({
    type:FETCH_PRODUCT_FAILURE,
    payload:error
})
// fetch pproducts
export const fetchProductData=()=>async(dispatch)=>{
    try{
        dispatch(fetchProductsRequest())
        const products =await fetchProducts()
        dispatch(fetchProductsSuccess(products))
    }
    catch{
        dispatch(fetchProductsFailure(err))
    }
}