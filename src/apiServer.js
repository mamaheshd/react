const API_URL ='https://fakestoreapi.com/products'

export const fetchProducts=async()=>{
    try{
        const response = await fetch(`${API_URL}`)
        const data= await response.jeson()
        return data
    }
    catch(err){
        console.error('Somthings went wrong',err)
    }
}