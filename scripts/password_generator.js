const{floor:entier}=Math;
random=(a=1,b=undefined)=>b?Math.random()*(b-a)+a:a*Math.random();
randomInt=(a,b)=>entier(random(a,b));
PasswordGenerator=(minLength=8,maxLength=8,character="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")=>
{
password=new Array(randomInt(minLength,maxLength))
for(i=0;i<password.length;i++)password[i]=character[randomInt(character.length)]
return password.join('');
}   

console.log("8 digit random alphanumeric password : "+PasswordGenerator());
console.log("random alphanumeric password of random length between 8 and 16 characters : "+PasswordGenerator(8,16));
console.log("8 digit random numeric password : "+PasswordGenerator(8,8,"0123456789"));
