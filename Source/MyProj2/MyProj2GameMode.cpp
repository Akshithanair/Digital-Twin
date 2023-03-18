// Copyright Epic Games, Inc. All Rights Reserved.

#include "MyProj2GameMode.h"
#include "MyProj2Character.h"
#include "UObject/ConstructorHelpers.h"

AMyProj2GameMode::AMyProj2GameMode()
{
	//set default pawn class to our Blueprinted character
	//static ConstructorHelpers::FClassFinder<APawn> PlayerPawnBPClass(TEXT("Class'/Script/MyProj2.MyPawn'"));
	//if (PlayerPawnBPClass.Class != NULL)
	//{
		//DefaultPawnClass = PlayerPawnBPClass.Class;
	//}
}
