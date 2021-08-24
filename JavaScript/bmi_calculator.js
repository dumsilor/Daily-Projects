/*
formula : BMI = wight(kg)/height^2 
*/ 
function bmiCalculator(weight,height){
    var height_in_menter = height*0.1;
    bmi = weight/height_in_menter**2;
    return bmi;
}