
@.procentD = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @main() #0 {
%a = alloca i32, align 4
store i32 5, i32* %a, align 4
%uniqmain1 = alloca i32, align 4
store i32 1, i32* %uniqmain1, align 4
%uniqamain2 = load i32, i32* %a, align 4
%uniquniqmain1main3 = load i32, i32* %uniqmain1, align 4
%uniqmain4 = add i32 %uniqamain2, %uniquniqmain1main3
store i32 %uniqmain4, i32* %a, align 4
%uniqamain5 = load i32, i32* %a, align 4
call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.procentD, i64 0, i64 0), i32 %uniqamain5)
ret i32 0
}