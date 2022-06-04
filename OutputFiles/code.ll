
@.uniqprintStringmain11 = private unnamed_addr constant [3 x i8] c"%i\00", align 1
declare dso_local i32 @__isoc99_scanf(i8*, ...) #1
@.procentC = private unnamed_addr constant [3 x i8] c"%c\00", align 1
@.procentF = private unnamed_addr constant [3 x i8] c"%f\00", align 1
declare dso_local i32 @printf(i8*, ...) #1
define i32 @test(i32 %parametera, i32 %parameterb) #0 {
	%a = alloca i32, align 4
	store i32 %parametera, i32* %a, align 4
	%b = alloca i32, align 4
	store i32 %parameterb, i32* %b, align 4
	%uniqreturnValuetest1 = alloca i32, align 4
	%uniqatest2 = load i32, i32* %a, align 4
	%uniqbtest3 = load i32, i32* %b, align 4
	%uniqtest4 = add i32 %uniqatest2, %uniqbtest3
	store i32 %uniqtest4, i32* %uniqreturnValuetest1, align 4
	%uniqreturnItemtest5 = load i32, i32* %uniqreturnValuetest1, align 4
	ret i32 %uniqreturnItemtest5
}
define i32 @main() #0 {
	%a = alloca [3 x i32], align 4
	%uniqindexmain1 = alloca i32, align 4
	store i32 0, i32* %uniqindexmain1, align 4
	%uniqindexmain2 = load i32, i32* %uniqindexmain1, align 4
	%temp1a= getelementptr inbounds [3 x i32], [3 x i32]* %a, i64 0, i32 %uniqindexmain2
store i32 3, i32* %temp1a, align 4
	%uniqindexmain3 = alloca i32, align 4
	store i32 1, i32* %uniqindexmain3, align 4
	%uniqindexmain4 = load i32, i32* %uniqindexmain3, align 4
	%temp3a= getelementptr inbounds [3 x i32], [3 x i32]* %a, i64 0, i32 %uniqindexmain4
store i32 3, i32* %temp3a, align 4
	%uniqindexmain5 = alloca i32, align 4
	store i32 2, i32* %uniqindexmain5, align 4
	%uniqindexmain6 = load i32, i32* %uniqindexmain5, align 4
	%temp5a= getelementptr inbounds [3 x i32], [3 x i32]* %a, i64 0, i32 %uniqindexmain6
store i32 10, i32* %temp5a, align 4
	%uniqreturnValuemain7 = alloca i32, align 4
	%temp6a= getelementptr inbounds [3 x i32], [3 x i32]* %a, i64 0, i32 +
%uniqparametermain8 = load i32, i32* %temp6a, align 4
	%temp7a= getelementptr inbounds [3 x i32], [3 x i32]* %a, i64 0, i32 1
%uniqparametermain9 = load i32, i32* %temp7a, align 4
	%uniqmain10 = call i32 @test(i32 %uniqparametermain8, i32 %uniqparametermain9)
	store i32 %uniqmain10, i32* %uniqreturnValuemain7, align 4
	%uniquniqreturnValuemain7main12 = load i32, i32* %uniqreturnValuemain7, align 4
	call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.uniqprintStringmain11, i64 0, i64 0) , i32 %uniquniqreturnValuemain7main12)
	ret i32 1
}